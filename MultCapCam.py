#!/usr/bin/python
"""Usage: MultCapCam.py [options] <Folder> [Step] [Duration]

Options:
  -h --help
  -v                 verbose mode
  --Step <int>       Time inter each capture[default: 60]
  --Duration <int>   Duration all capture proces[default: 300]
"""
from docopt import docopt
import errno
import os
from os import path
from picamera import PiCamera
import time as time


#def main():
arguments = docopt(__doc__)

path = arguments['<Folder>']

try:
    os.mkdir(path)
except OSError as e:
    if e.errno == errno.EEXIST:
        pass

Step = int(arguments['--Step']) 
Duration = int(arguments['--Duration'])

Final=Duration/Step

camera = PiCamera()
camera.start_preview(alpha=192)

cont=0
while(cont<=Final):
    print(time.time(),time.strftime("%d-%m-%Y,%H:%M:%S"))
    time.sleep(2)
    camera.capture(path+"/S"+time.strftime("%d-%m-%Y,%H:%M:%S")+".jpg")
    camera.stop_preview()
    cont=cont+1
    time.sleep(Step-2)

#if __name__ == '__main__':
#    app.run(main)    