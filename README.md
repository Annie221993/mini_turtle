# Mini Turtle

Este proyecto corresponde al *Ejercicio 1 – Versión Funcional* de la tarea Mini-Turtle.

El objetivo es aplicar *modularidad en Python*, separando la lógica interna y la interfaz pública del paquete.

## Contenido del paquete

- adelante(pasos): aumenta la posición de la tortuga
- abajo(): simula bajar el lápiz
- reiniciar(): reinicia la posición a cero

## Ejemplo de uso

```python
from mini_turtle import adelante, abajo, reiniciar

adelante(4)
abajo()
adelante(2)
reiniciar()
adelante(3)
