import os
import glob
import time
import RPi.GPIO as GPIO

#these tow lines mount the device:
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_path = glob.glob(base_dir + '28*')[0] #get file path of sensor
rom = device_path.split('/')[-1] #get rom name

def read_temp_raw():
    with open(device_path +'/w1_slave','r') as f:
        valid, temp = f.readlines()
    return valid, temp
 
def read_temp():
    valid, temp = read_temp_raw()

    while 'YES' not in valid:
        time.sleep(0.2)
        valid, temp = read_temp_raw()

    pos = temp.index('t=')
    if pos != -1:
        #read the temperature .
        temp_string = temp[pos+2:]
        temp_c = float(temp_string)/1000.0 
        temp_f = temp_c * (9.0 / 5.0) + 32.0
        return temp_c, temp_f
 
def maintemp():
    print(' ROM: '+ rom)

    while True:
        c, f = read_temp()
        print('C={:,.3f} F={:,.3f}'.format(c, f))
        time.sleep(1)

# cold shit
def gpio3():
    GPIO.setup(3, GPIO.OUT)
    GPIO.output(3, GPIO.LOW) # ON
    time.sleep(5)
    GPIO.output(3, GPIO.HIGH) # OFF

# hot shit
def gpio5():
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, GPIO.LOW) # ON
    time.sleep(5)
    GPIO.output(5, GPIO.HIGH) # OFF

def test():
    GPIO.setmode(GPIO.BOARD)
    gpio3()
    GPIO.cleanup()

def main():
    temp, _ = read_temp()
    print(temp)
    x = int(input("Please input the temperature: "))
    t = int(input("Please input the time: "))
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    start = time.time()
    while True:
        GPIO.setmode(GPIO.BOARD)
        temp, _ = read_temp()
        print(temp)
        if (temp <= x):
            GPIO.output(5, GPIO.LOW) # open 5
            print("OPEN HOT WATER")
            GPIO.output(3, GPIO.HIGH) # close 3
            print("CLOSE COLD WATER")
        if (temp >= x):
            GPIO.output(3, GPIO.LOW) # open 3
            print("OPEN COLD WATER")
            GPIO.output(5, GPIO.HIGH) # close 5
            print("CLOSE HOT WATER")
        end = time.time()
        if (end - start >= t):
            GPIO.output(3, GPIO.HIGH) # close 3
            GPIO.output(5, GPIO.HIGH) # close 5
            GPIO.cleanup()
            break

main()
