class Tortuga:
    def _init_(self):
        self.posicion_x = 0

    def adelante(self, pasos):
        self.posicion_x += pasos
        print(f"Tortuga avanza {pasos} pasos. Posición actual: {self.posicion_x}")

    def abajo(self):
        print("Tortuga baja el lápiz")
