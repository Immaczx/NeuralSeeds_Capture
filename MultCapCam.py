#!/usr/bin/python3
# Menu docopt
"""Usage: MultCapCam.py [options] <Folder> [Step] [Duration]

Options:
  -h --help
  -v                 verbose mode
  --Step <int>       Time inter each capture, use d, h, m for day, hour, minute respectively [default: 10]
  --Duration <int>   Duration all capture proces, use d, h, m for day, hour, minute respectively [default: 50]
"""
from docopt import docopt # interface comandos
import errno # Gestion errores
import os # comunicacioncon teminal
from os import path 
from picamera import PiCamera # Camara socket Rasp
import time as time
from gpiozero import LED # funcion led Del GPIO 

def code_time(time): # Funcion pasar timepo a segundos
    if time[-1] == 'd': timeSeg = float(time[:-1])*86400 
    elif time[-1] == 'h': timeSeg = float(time[:-1])*3600
    elif time[-1] == 'm': timeSeg = float(time[:-1])*60
    else: timeSeg = float(time) 

    return timeSeg

#def main():
arguments = docopt(__doc__) # Almacenar diccionario docopt

path = arguments['<Folder>'] # Almacenar carpeta donde se desea guardar

try:  # Intentar crear carpeta
    os.mkdir(path) 
except OSError as e: # existe error
    if e.errno == errno.EEXIST: # si error es  carpeta existe entonces ... 
        pass  # continuar

Step = code_time(arguments['--Step']) # se transforma a segundos y almacena el intervalo de capturas
Duration = code_time(arguments['--Duration']) # se transforma a segundos y alamcena La duracion de la secion de capturas

flash = LED(17) # pin Para conectar Flash

Final=Duration/Step # Cantidad de capturas

camera = PiCamera() # Objeto camara
camera.start_preview(alpha=192) # preview

cont=0 # contador capturas
while(cont<=Final):
    # print(time.time(),time.strftime("%d-%m-%Y,%H:%M:%S"))
    time.sleep(1.5) # Espara un segundo y medio
    flash.on()  # ensender Flash
    time.sleep(0.2) # esperar
    camera.capture(path+"/S"+time.strftime("%d-%m-%Y,%H:%M:%S")+".jpg") # Capturar imgen
    flash.off() # Apagar Flash
    camera.stop_preview() # detenener preview
    time.sleep(0.2) # esperar
    cont=cont+1 # aumentar contador capturas 
    
    time.sleep(Step-2) # Esperar step -2 seguntos

#if __name__ == '__main__':
#    app.run(main)    
