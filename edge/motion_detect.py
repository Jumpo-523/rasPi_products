# -*- coding: utf-8 -*-

from datetime import datetime
import time
import RPi.GPIO as GPIO



def motion_detect():
    # インターバル
    INTERVAL = 3
    # スリープタイム
    SLEEPTIME = 2
    # 使用するGPIO
    GPIO_PIN = 18

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.IN)
    detected = False
    try:
        cnt = 1
        while cnt < 10:
            # センサー感知
            if(GPIO.input(GPIO_PIN) == GPIO.HIGH):
                print(datetime.now().strftime('%Y/%m/%d %H:%M:%S') +
                "：" + str("{0:05d}".format(cnt)) + "回目の人感知")
                detected = True
                time.sleep(SLEEPTIME)
            else:
                print(GPIO.input(GPIO_PIN))
                time.sleep(INTERVAL)
            cnt = cnt + 1
    except KeyboardInterrupt:
        print("終了処理中...")
    finally:
        GPIO.cleanup()
        print("GPIO clean完了")
    
    return detected
