posicion_x = 0

def adelante(pasos):
    global posicion_x
    posicion_x = posicion_x + pasos
    print(posicion_x)

def abajo(pasos):
    print("abajo")

def reiniciar():
    global posicion_x
    posicion_x = 0
