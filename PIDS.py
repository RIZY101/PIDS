# Written by Richard Zins for PIDS
import RPi.GPIO as GPIO
import time
import datetime
import subprocess
from picamera import PiCamera
import Text
import Email

cam = PiCamera()
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
PIR_PIN = 13
GPIO.setup(PIR_PIN, GPIO.IN)

print('Starting PIDS Console')
time.sleep(1)
print ('Ready')

counter = 1
while True:
    if GPIO.input(PIR_PIN) and counter == 1:
        print('Motion Detected')
        imageName = str(datetime.datetime.now()) + '.jpg'
        path = '/var/www/html/intrusions/' + imageName
        cam.capture(path)
        counter = counter + 1
        try: 
            Text.send()
            Email.send()
        except:
            print('An unnexpected error occured when sending a text or email alert')
    elif GPIO.input(PIR_PIN) and counter > 1 and counter <= 3:
        print('Motion Detected')
        imageName = str(datetime.datetime.now()) + '.jpg'
        path = '/var/www/html/intrusions/' + imageName
        cam.capture(path)
        counter = counter + 1 
    elif GPIO.input(PIR_PIN) and counter > 3:
        print('Motion Detected')
        print('Starting Video Capture')
        cam.start_recording('/var/www/html/video.h264')
        time.sleep(30)
        cam.stop_recording()
        subprocess.call("./convert.sh")
        counter = 1
        print('Capture Stopped And Uploaded To Website')
    time.sleep(1)
        
