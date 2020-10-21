from picamera import PiCamera

import time
# configuration of picamera.
# https://www.pc-koubou.jp/magazine/17276


# 赤外線距離センサー
# RFR-359F ----- RaspberryPi GPIO
#=SIG ---13
#=NC
#=VCC ---2
#=GND ---20

import time
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BOARD)
SIG = 13
GPIO.setup(13, GPIO.IN)


cnt = 0
path = f"/home/pi/Desktop/image_{cnt}.jpg"



def take_photo(path):
    if GPIO.input(SIG) == 0:
        camera = PiCamera()
        camera.start_preview()
        time.sleep(5*60)
        camera.capture(path)
        camera.stop_preview()
    else:
        print("somthing wrong in PIN 13")



if __name__ == "__main__":
    # test_take
    take_photo(path)