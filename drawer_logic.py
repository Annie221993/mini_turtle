# drawer_logic.py
# Aquí va la lógica de dibujo

posicion_x = 0

def adelante(pasos=50):
    global posicion_x
    posicion_x += pasos
    print(f"Tortuga avanza a la posición {posicion_x}")

def abajo():
    print("Tortuga baja una línea")

def reiniciar():
    global posicion_x
    posicion_x = 0
    print("Posición reiniciada a 0")
