import turtle
circle = turtle.Turtle()
circle1 = turtle.Turtle()
circle2 = turtle.Turtle()
circle.speed(400)
circle1.speed(400)
circle2.speed(400)
circle.pensize(2)
circle.getscreen().bgcolor("Black")
circle.penup()
circle.goto(0, 1)
circle.pendown()
colors = ["red", "green", "blue", "orange", "white", "grey", "palegreen", "lightblue"]

for i in range(75):
    circle.pencolor(colors[i % len(colors)])
    circle.circle(70)
    circle.forward(100)
    circle.left(20)
    circle.right(90)
    circle.forward(60)
    circle.circle(30)

circle1.penup()
circle1.goto(-500, 100)
circle1.pendown()

for i in range(75):
    circle1.pencolor(colors[i % len(colors)])
    circle1.circle(70)
    circle1.forward(100)
    circle1.left(20)
    circle1.right(90)
    circle1.forward(60)
    circle1.circle(30)

circle2.penup()
circle2.goto(500, 100)
circle2.pendown()

for i in range(75):
    circle2.pencolor(colors[i % len(colors)])
    circle2.circle(70)
    circle2.forward(100)
    circle2.left(20)
    circle2.right(90)
    circle2.forward(60)
    circle2.circle(30)

turtle.done()