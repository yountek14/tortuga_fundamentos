import turtle

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pikachu by @AI")
p = turtle.Turtle()
p.speed(10)
p.pensize(3)

# Función para dibujar formas elípticas (para cuerpo y cabeza)
def oval(t, size_x, size_y, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(size_x, 90)
        t.circle(size_y, 90)
    t.end_fill()

# Función para dibujar orejas
def ear(t, length, angle, color):
    t.setheading(angle)
    t.color(color)
    t.begin_fill()
    t.forward(length)
    t.right(120)
    t.forward(length * 0.6)
    t.right(120)
    t.forward(length)
    t.end_fill()

# Cabeza principal
p.penup()
p.goto(0, -100)
p.pendown()
oval(p, 60, 100, "#FFD700")  # Amarillo Pikachu

# Orejas
p.penup()
p.goto(-40, 120)
p.pendown()
ear(p, 80, 60, "black")  # Parte negra de oreja izquierda
p.color("#FFD700")
p.begin_fill()
ear(p, 70, 60, "#FFD700")  # Parte amarilla
p.end_fill()

p.penup()
p.goto(40, 120)
p.pendown()
ear(p, 80, 120, "black")  # Oreja derecha
p.color("#FFD700")
p.begin_fill()
ear(p, 70, 120, "#FFD700")
p.end_fill()

# Ojos
def eye(x, y):
    p.penup()
    p.goto(x, y)
    p.pendown()
    p.color("black")
    p.begin_fill()
    p.circle(15)
    p.end_fill()
    
    # Brillo ocular
    p.penup()
    p.goto(x + 5, y + 20)
    p.color("white")
    p.begin_fill()
    p.circle(4)
    p.end_fill()

eye(-25, 40)
eye(25, 40)

# Mejillas rojas
p.penup()
p.goto(-50, 0)
p.color("#FF0000")
p.begin_fill()
p.circle(10)
p.end_fill()

p.goto(50, 0)
p.begin_fill()
p.circle(10)
p.end_fill()

# Boca sonriente
p.penup()
p.goto(-25, -20)
p.pendown()
p.right(90)
p.color("black")
p.width(4)
p.circle(25, 180)

# Cuerpo
p.penup()
p.goto(0, -160)
p.pendown()
oval(p, 80, 120, "#FFD700")

# Brazos
def arm(x, angle):
    p.penup()
    p.goto(x, -120)
    p.setheading(angle)
    p.pendown()
    p.color("#FFD700")
    p.begin_fill()
    p.forward(40)
    p.left(90)
    p.forward(20)
    p.left(90)
    p.forward(40)
    p.end_fill()

arm(-70, 150)
arm(70, 30)

# Piernas
p.penup()
p.goto(-40, -240)
p.color("#FFD700")
p.begin_fill()
p.circle(20)
p.end_fill()

p.goto(40, -240)
p.begin_fill()
p.circle(20)
p.end_fill()

# Cola (forma de rayo)
def draw_tail():
    p.penup()
    p.goto(120, -180)
    p.pendown()
    p.color("#8B4513")  # Café para base
    p.begin_fill()
    p.setheading(45)
    p.forward(40)
    p.right(90)
    p.forward(20)
    p.right(90)
    p.forward(40)
    p.end_fill()
    
    # Parte eléctrica
    p.color("black")
    p.penup()
    p.goto(160, -140)
    p.pendown()
    p.begin_fill()
    p.setheading(60)
    for _ in range(4):
        p.forward(30)
        p.right(90)
        p.forward(30)
        p.left(90)
    p.end_fill()

draw_tail()

p.hideturtle()
turtle.done()