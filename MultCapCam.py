#!/usr/bin/python
"""
Created on Sat Oct  2 12:22:24 2021

@author: Camilo
"""
from absl import app, flags, logging
from absl.flags import FLAGS
import errno
import os
from os import path
from picamera import PiCamera
import time as time


flags.DEFINE_string('Path',"/home/pi/Desktop/test",'Path make o extis path')
flags.DEFINE_integer('Step',60,'Time inter each capture')
flags.DEFINE_integer('Duration',300,'Duration all capture proces')

def main(_argv):
    
    path = FLAGS.Path
    
    try:
        os.mkdir(path)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass

    Step = FLAGS.Step 
    Duration = FLAGS.Duration
    
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

if __name__=="__main__":
    app.run(main)