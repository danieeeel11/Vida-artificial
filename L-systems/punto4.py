import turtle
import random

# Define funciones para generar diferentes tipos de árboles con sistemas-L

def arbol_tipo1(t, longitud, angulo, nivel):
    if nivel > 0:
        t.forward(longitud)
        t.left(angulo)
        arbol_tipo1(t, longitud * 0.7, angulo, nivel - 1)
        t.right(2 * angulo)
        arbol_tipo1(t, longitud * 0.7, angulo, nivel - 1)
        t.left(angulo)
        t.backward(longitud)

def arbol_tipo2(t, longitud, angulo, nivel):
    if nivel > 0:
        t.forward(longitud)
        t.right(angulo)
        arbol_tipo2(t, longitud * 0.5, angulo, nivel - 1)
        t.left(2 * angulo)
        arbol_tipo2(t, longitud * 0.5, angulo, nivel - 1)
        t.right(angulo)
        t.backward(longitud)

def arbol_tipo3(t, longitud, angulo, nivel):
    if nivel > 0:
        t.forward(longitud)
        t.left(angulo)
        arbol_tipo3(t, longitud * 0.3, angulo, nivel - 1)
        t.right(angulo * 2)
        arbol_tipo3(t, longitud * 0.3, angulo, nivel - 1)
        t.left(angulo)
        t.backward(longitud)

# Configuración de la ventana
wn = turtle.Screen()
wn.bgcolor("white")

# Crear un objeto Turtle
t = turtle.Turtle()
t.speed(0)  

# Configuración de la posición inicial y ángulo
t.penup()
t.goto(0, -200)
t.pendown()
t.left(90)

# Colores para los árboles
colores_arboles = ["#CC5500", "maroon", "forestgreen"]

# Dibuja varios árboles en el bosque
for _ in range(50):
    t.color(random.choice(colores_arboles))
    arbol_tipo = random.randint(1, 3) 
    if arbol_tipo == 1:
        arbol_tipo1(t, 100, 25, 9)
    elif arbol_tipo == 2:
        arbol_tipo2(t, 50, 15, 7)
    else:
        arbol_tipo3(t, 100, 35, 9)
    t.penup()
    t.goto(random.randint(-300, 300), -200) 
    t.pendown()

# Cerrar la ventana cuando se haga clic
wn.exitonclick()
