import turtle
pegasus  = turtle.Turtle()
pegasus.getscreen().bgcolor("gray")
pegasus.color("lightblue", "blue")

pegasus.penup()
pegasus.goto((-200, 100 ))
pegasus.pendown()
pegasus.speed(100)

pegasus.begin_fill()
def star(turtle, size):
    if size <= 10:
        return
    else: 
        for i in range(5):
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
pegasus.end_fill()
star(pegasus, 360)


turtle.done()