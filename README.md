# NeuralSeeds_Capture

Este codigo permite realizar una sesión de capturas sobre una Raspberry pi 4, usando una camara conectara a su socket y habilitanto el pin 17 como triger de un Flash.
En el script podremos definir:

Ubicacion de las capturas <Folder>

Inetervalos de captura --Step

Duracion de la sesión --Duration

Si usamos el comando -h o --help retornara esta descripción:

´´´Usage: MultCapCam.py [options] <Folder> [Step] [Duration]
Options:
  -h --help
  -v                 verbose mode
  --Step <int>       Time inter each capture, use d, h, m for day, hour, minute respectively [default: 10]
  --Duration <int>   Duration all capture proces, use d, h, m for day, hour, minute respectively [default: 50]
´´´
