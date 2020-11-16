# parking sensor

## goal

use an ultrasonic distance sensor (I used this one: [SainSmart HC-SR04 Ranging Detector Mod Distance Sensor](https://smile.amazon.com/gp/product/B004U8TOE6/ref=ppx_yo_dt_b_asin_title_o00_s00)) to turn on LED lights to indicate that you're "close enough" when pulling into the garage. Green indicates "plenty of room", yellow indicates "getting close", and red indicates "too close."


## references
- [original Instructable](https://www.instructables.com/Raspberry-Pi-Park-Sensor/)

## helper commands

To copy from pi:
`scp pi@<ip>:Desktop/parking-sensor.py .`

To copy to pi:
`scp parking-sensor.py pi@<ip>:Desktop/`