import turtle

# Definimos las reglas de producción
def apply_rules(s):
    new_s = ""
    for char in s:
        if char == 'F':
            new_s += 'FF+[+F-F-F]-[-F+F+F]'
        else:
            new_s += char
    return new_s

# Configuramos el sistema
initial_string = "F"
iterations = 4
step_length = 18

# Inicializamos la tortuga
t = turtle.Turtle()
t.goto(-300,0)
screen = turtle.Screen()
screen.tracer(0)

# Implementamos el sistema de interpretación con pila
stack = []

for _ in range(iterations):
    initial_string = apply_rules(initial_string)

for char in initial_string:
    if char == 'F':
        t.forward(step_length)
    elif char == '+':
        t.left(22.5)  # Ángulo modificado a 22.5 grados
    elif char == '-':
        t.right(22.5)  # Ángulo modificado a 22.5 grados
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
