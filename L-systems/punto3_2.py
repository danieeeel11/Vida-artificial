import turtle
import random

# Definimos las reglas de producción con probabilidades
rules = {
    'F': [
        ('F[+F[+F]-F][-F]F', 1),
    ]
    #'+': [('+', 1)],
    #'-': [('-', 1)],
    #'[': [('[', 1)],
    #']': [('[', 1)],
}

# Configuramos el sistema
initial_string = "F"
iterations = 4
step_length = 25

# Inicializamos la tortuga
t = turtle.Turtle()
t.goto(-300,0)
screen = turtle.Screen()
screen.tracer(0)

# Implementamos el sistema de interpretación con pila
stack = []

for _ in range(iterations):
    new_string = ""
    for char in initial_string:
        rule_choices = rules.get(char, [(char, 1)])
        selected_rule = random.choices(*zip(*rule_choices))[0]
        new_string += selected_rule
    initial_string = new_string

for char in initial_string:
    if char == 'F':
        t.forward(step_length)
    elif char == '+':
        t.left(25)  # Ángulo originalmente definido en 25 grados
    elif char == '-':
        t.right(25)  # Ángulo originalmente definido en 25 grados
    elif char == '[':
        stack.append((t.position(), t.heading()))
    elif char == ']':
        position, heading = stack.pop()
        t.penup()
        t.goto(position)
        t.setheading(heading)
        t.pendown()

# Mostramos el resultado
screen.update()
turtle.done()
