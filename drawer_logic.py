# mini_turtle/drawer_logic.py

# Variable global que guarda la posición
posicion_x = 0

def adelante(pasos):
    global posicion_x
    posicion_x += pasos
    print(f"Avanzando {pasos} pasos → Posición actual: {posicion_x}")

def abajo():
    print("Bajando una línea")

def reiniciar():
    global posicion_x
    posicion_x = 0
    print("Posición reiniciada a 0")
