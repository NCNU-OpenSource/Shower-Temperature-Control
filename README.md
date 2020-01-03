[NCNU LSA project]  一起洗澡吧>///<
===
## Idea
洗澡, 洗香香~ 一個便宜精準的控溫方案！

<<調水溫>> 自古至今都是一件極度艱鉅的任務, 此專案旨在解決此難題。
使用者可輸入自己偏愛的溫度, 甚至設置多組個人設定, 共浴時不再需煩惱太冷/太熱的水溫。
多人使用, 效果尤佳。

## How to use?
Input temperature & expected time of shower, then wait for the magic!

## Group member
- 李柏翰 106213001
- 游允喆 106213021
- 吳翰琳 106213060
- 黃暐澄 106213076

## Hardware
| 名稱           | 數量 | 來源     |
| -------------- | ---- | -------- |
| Raspberry Pi 3     | 1    | 課堂提供 |
| Temperature Sensor (DS18B20)| 1    | https://www.taiwaniot.com.tw/product/100cm長度-ds18b20防水探針型熱電偶溫度感測器/   |
| 微型 抽水馬達 沉水馬達(立式) DC3V~DC5V     | 2    | https://www.taiwaniot.com.tw/product/微型-抽水馬達-沉水馬達-dc3vdc5v/ |
| Relay    | 2    | MOLi |
| 水管     | 很長  | 柏翰  |
| 寶特瓶   | 2    | 全家, MOLi桌上 |
| Dupont Wire    | 數根   | MOLi |

## Packages
Python
  - RPi.GPIO  ```pip3 install RPi.GPIO```
  - os
  - glob
  - time

## Circuit diagram

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

## Future/Potential improvements
  - 溫度計反應太慢 → [更多的溫度計] Cold, Hot 兩鍋各放一支溫度計, 依此決定馬達啓閉
  - 淋浴停止時間預輸入 → [水位感測] 依水位感測判斷使用者是否已關閉水源, 發現關水程式就自動停止。現有方式爲使用者輸入一預期終止時間來停止程式, 不甚理想。 
  - 人物判斷 → 判斷蓮蓬頭下的使用者, 自動 apply 使用者設定

## References
  https://www.youtube.com/watch?v=j7LLVkPpQ78&t=481s
  
  https://pypi.org/project/RPi.GPIO/
  
  https://tutorials-raspberrypi.com/raspberry-pi-temperature-sensor-1wire-ds18b20/
  
