#!/usr/bin/python3
"""Usage: MultCapCam.py [options] <Folder> [Step] [Duration]

Options:
  -h --help
  -v                 verbose mode
  --Step <int>       Time inter each capture, use d, h, m for day, hour, minute respectli [default: 10]
  --Duration <int>   Duration all capture proces, use d, h, m for day, hour, minute respectli [default: 50]
"""
from docopt import docopt
import errno
import os
from os import path
from picamera import PiCamera
import time as time
import RPi.GPIO as GPIO

def code_time(time):
    if time[-1] == 'd': timeSeg = float(time[:-1])*86400 
    elif time[-1] == 'h': timeSeg = float(time[:-1])*3600
    elif time[-1] == 'm': timeSeg = float(time[:-1])*60
    else: timeSeg = float(time) 

    return timeSeg

#def main():
arguments = docopt(__doc__)

path = arguments['<Folder>']

try:
    os.mkdir(path)
except OSError as e:
    if e.errno == errno.EEXIST:
        pass

Step = code_time(arguments['--Step']) 
Duration = code_time(arguments['--Duration'])
flash = 23

Final=Duration/Step
# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(flash, GPIO.OUT)

camera = PiCamera()
camera.start_preview(alpha=192)

cont=0
while(cont<=Final):
    print(time.time(),time.strftime("%d-%m-%Y,%H:%M:%S"))
    time.sleep(1)
    GPIO.output(flash, GPIO.HIGH)
    time.sleep(2)
    camera.capture(path+"/S"+time.strftime("%d-%m-%Y,%H:%M:%S")+".jpg")
    GPIO.output(flash, GPIO.LOW)
    camera.stop_preview()
    time.sleep(0.2)
    cont=cont+1
    
    time.sleep(Step-2)

#if __name__ == '__main__':
#    app.run(main)    
