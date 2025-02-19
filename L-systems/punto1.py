import turtle

def generate_string(axiom, production_rules, iterations):
    result = axiom

    for _ in range(iterations):
        result = ''.join(production_rules.get(c, c) for c in result)

    return result

def interpret_string(input_string, angle, size):
    turtle.speed(0)
    stack = []

    for char in input_string:
        if char == 'F':
            turtle.forward(size)
        elif char == '-':
            turtle.left(angle)
        elif char == '+':
            turtle.right(angle)
        elif char == '[':
            stack.append((turtle.position(), turtle.heading()))
        elif char == ']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.goto(position)
            turtle.setheading(heading)
            turtle.pendown()

if __name__ == "__main__":
    axiom = 'FX'
    production_rules = {'X': 'X+YF', 'Y': 'FX-Y'}
    iterations = 10
    result = generate_string(axiom, production_rules, iterations)

    turtle.speed(0) 
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()

    interpret_string(result, 90, 10)

    turtle.done()