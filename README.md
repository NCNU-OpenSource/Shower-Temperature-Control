NCNU LSA project - 一起洗澡吧>///<
===
## Idea
洗澡，洗香香~ 

<<調水溫>>自古至今都是一件極度艱鉅的任務,此專案旨在解決此難題。
多人使用，效果尤佳。

## How to use?
Input temperature & expected time of shower, then wait for the magic!

## Group member
- 李柏翰 106213001
- 游允喆 106213021
- 吳翰琳 106213060
- 黃暐澄 106213076

## Hardware
  - Raspberry Pi 3
  - Temperature Sensor (DS18B20) × 1          https://www.taiwaniot.com.tw/product/微型-抽水馬達-沉水馬達-dc3vdc5v/
  - 微型 抽水馬達 沉水馬達(立式) DC3V~DC5V × 2    https://www.taiwaniot.com.tw/product/100cm長度-ds18b20防水探針型熱電偶溫度感測器/
  - Relay × 2

## Packages
Python
  - RPi.GPIO  ```pip3 install RPi.GPIO```
  - os
  - glob
  - time

## 電路圖

## Temperature Sensor (DS18B20) set up
 - 接好電路板
 - sudo vim /boot/config.txt
    - 加入 ```dtoverlay=w1.gpio``` 後 reboot
 ```=
 .
 .
 .
 dtoverlay=w1.gpio
 ```
 - ```sudo modprobe w1-gpio ```
 - ```sudo modprobe w1-therm```
 - ```cd /sys/bus/w1/devices/28-XXXXXXXXX```    //若電路板未加電阻 devices 只會顯示 00-XXXXXXXXX
 - ```cat w1_slave```

## functions & code explained
  - ```GPIO.setmode(GPIO.BOARD)```  //GPIO腳位編號有 BCM 跟 BOARD 兩種模式
                                GPIO.BOARD: PIN腳位編號  電路版上接脚的號碼  GPIO.BCM: 指定GPIO後面的號碼
  - ```GPIO.setup(x, GPIO.OUT)```   //Input or Output
  - ```GPIO.output(x, GPIO.LOW)```  //High or Low
  
  - ```read(ds18b20)[0]```          //[0]celsius, [1]farenheit
  
## Future improvements
  - 解決溫度計反應太慢的問題 → [更多的溫度計] Cold, Hot 兩鍋各放一支溫度計
  - 水位感測 → 現有方式爲設定

## References
  https://www.youtube.com/watch?v=j7LLVkPpQ78&t=481s
  https://pypi.org/project/RPi.GPIO/
  https://tutorials-raspberrypi.com/raspberry-pi-temperature-sensor-1wire-ds18b20/
  
