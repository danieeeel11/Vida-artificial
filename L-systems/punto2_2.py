import turtle

# Definición de las reglas de producción y parámetros
axiom = 'F+F+F+F'
production_rules = {'F': 'F+F+F-FFF-F'}
iterations = 3
angle = 90
size = 10

# Función para aplicar las reglas de producción
def apply_production_rules(axiom, production_rules, iterations):
    result = axiom
    for _ in range(iterations):
        next_result = []
        for char in result:
            next_result.append(production_rules.get(char, char))
        result = ''.join(next_result)
    return result

# Función para interpretar la cadena y dibujar el patrón
def interpret_string(input_string, angle, size):
    t = turtle.Turtle()
    t.speed(0)
    t.setheading(90)  # Orientación inicial hacia arriba
    
    # Centrar la tortuga en la posición x
    t.penup()
    t.setx(0)
    t.pendown()
    
    stack = []

    for char in input_string:
        if char == 'F':
            t.forward(size)
        elif char == '-':
            t.left(angle)
        elif char == '+':
            t.right(angle)
        elif char == '[':
            stack.append((t.position(), t.heading()))
        elif char == ']':
            position, heading = stack.pop()
            t.penup()
            t.goto(position)
            t.setheading(heading)
            t.pendown()

    t.hideturtle()
    turtle.done()

# Aplicar reglas de producción
resulting_string = apply_production_rules(axiom, production_rules, iterations)

# Interpretar la cadena y dibujar el patrón
interpret_string(resulting_string, angle, size)