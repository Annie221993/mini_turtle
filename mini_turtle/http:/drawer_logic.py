 # mini_turtle/drawer_logic.py

posicion_x = 0  # variable global

def adelante(pasos):
    global posicion_x
    posicion_x += pasos
    print(f"Avanzando {pasos} pasos. Posición actual: {posicion_x}")

def abajo():
    print("Bajando el lápiz")

def reiniciar():
    global posicion_x
    posicion_x = 0
    print("Posición reiniciada a 0")
