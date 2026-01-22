import turtle

shapes = turtle.Turtle()
shapes.color("red", "lightblue")

shapes.getscreen().bgcolor("yellow")

shapes.begin_fill()
shapes.speed(1000)
for i in range(100):
    shapes.left(120)
    shapes.forward(150)
    shapes.left(130)
    shapes.forward(150)

shapes.end_fill()
shapes.penup()
shapes.goto(200, -150)
shapes.pendown()

for i in range(60):
    shapes.forward(150)
    shapes.right(150)
    shapes.forward(150)
    shapes.right(130)
    shapes.forward(150)
    shapes.right(160)
    shapes.forward(150)
    shapes.right(150)
    shapes.forward(150)

shapes.penup()
shapes.goto(0, 300)
shapes.pendown()

shapes.speed(20)
shapes.circle(50)
shapes.forward(40)

shapes.penup()
shapes.goto(-250, -190)
shapes.pendown() 

for i in range(100):
    shapes.forward(70)
    shapes.left(90)
    shapes.forward(90)
    shapes.left(200)
    shapes.forward(70)


turtle.done()