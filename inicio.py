import turtle
import random
import time

# CONFIGURACIÓN DEL MUNDO
GRID_SIZE = 20  # Tamaño de la grilla (20x20)
CELL_SIZE = 20  # Tamaño en píxeles de cada celda
DELAY = 0.2     # Delay entre generaciones

# Creamos ventana
pantalla = turtle.Screen()
pantalla.title("Juego de la Vida - Conway")
pantalla.bgcolor("white")
pantalla.setup(width=GRID_SIZE * CELL_SIZE + 50, height=GRID_SIZE * CELL_SIZE + 50)
pantalla.tracer(0)

# Lápiz para dibujar
lapiz = turtle.Turtle()
lapiz.penup()
lapiz.hideturtle()
lapiz.speed(0)

# Inicializar matriz con ceros y algunos vivos aleatorios
def crear_matriz():
    return [[random.choice([0, 1]) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def contar_vecinos(matriz, x, y):
    vecinos = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                vecinos += matriz[nx][ny]
    return vecinos

def actualizar(matriz):
    nueva = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            vivos = contar_vecinos(matriz, x, y)
            if matriz[x][y] == 1 and vivos in [2, 3]:
                nueva[x][y] = 1
            elif matriz[x][y] == 0 and vivos == 3:
                nueva[x][y] = 1
    return nueva

def dibujar_matriz(matriz):
    lapiz.clear()
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if matriz[x][y] == 1:
                dibujar_celda(x, y, "black")
            else:
                dibujar_celda(x, y, "white")
    pantalla.update()

def dibujar_celda(x, y, color):
    lapiz.goto(
        x * CELL_SIZE - (GRID_SIZE * CELL_SIZE) // 2,
        y * CELL_SIZE - (GRID_SIZE * CELL_SIZE) // 2
    )
    lapiz.fillcolor(color)
    lapiz.begin_fill()
    for _ in range(4):
        lapiz.forward(CELL_SIZE)
        lapiz.right(90)
    lapiz.end_fill()

# INICIAR SIMULACIÓN
matriz = crear_matriz()
while True:
    dibujar_matriz(matriz)
    matriz = actualizar(matriz)
    time.sleep(DELAY)
