import turtle
square = turtle.Turtle()

square.color("lightblue", "brown")

square.begin_fill()
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)

square.penup()
square.forward(100)
square.pendown()

square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.left(90)
square.forward(100)
square.end_fill()

turtle.done()