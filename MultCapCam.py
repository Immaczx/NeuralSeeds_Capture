#!/usr/bin/python3
"""Usage: MultCapCam.py [options] <Folder> [Step] [Duration]

Options:
  -h --help
  -v                 verbose mode
  --Step <int>       Time inter each capture, use d, h, m for day, hour, minute respectively [default: 10]
  --Duration <int>   Duration all capture proces, use d, h, m for day, hour, minute respectively [default: 50]
"""
from docopt import docopt
import errno
import os
from os import path
from picamera import PiCamera
import time as time
from gpiozero import LED

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
flash = LED(17)

Final=Duration/Step

camera = PiCamera()
camera.start_preview(alpha=192)

cont=0
while(cont<=Final):
    print(time.time(),time.strftime("%d-%m-%Y,%H:%M:%S"))
    time.sleep(1)
    flash.on()
    time.sleep(2)
    camera.capture(path+"/S"+time.strftime("%d-%m-%Y,%H:%M:%S")+".jpg")
    flash.off()
    camera.stop_preview()
    time.sleep(0.2)
    cont=cont+1
    
    time.sleep(Step-2)

#if __name__ == '__main__':
#    app.run(main)    
