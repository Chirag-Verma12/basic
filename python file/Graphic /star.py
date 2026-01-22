import turtle
import math

star = turtle.Turtle()

star.color("lightblue", "red")
star.begin_fill()
star.speed(200000)
star.getscreen().bgcolor("yellow")

for i in range(2000):
    star.forward(10)
    star.left(math.sin(i/10)*25)
    star.left(20)

star.end_fill()

turtle.done()