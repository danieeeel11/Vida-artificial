import turtle

# Definimos las reglas de producción
def apply_rules(s):
    new_s = ""
    for char in s:
        if char == 'F':
            new_s += 'F[+F]F[-F[+F][-F]]F'
        else:
            new_s += char
    return new_s

# Configuramos el sistema
initial_string = "F"
iterations = 4
step_length = 10

# Inicializamos la tortuga
t = turtle.Turtle()
t.goto(-500,0)
screen = turtle.Screen()
screen.tracer(0)

# Implementamos el sistema de interpretación
stack = []

for _ in range(iterations):
    initial_string = apply_rules(initial_string)

for char in initial_string:
    if char == 'F':
        t.forward(step_length)
    elif char == '+':
        t.left(25)
    elif char == '-':
        t.right(25)
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
