import turtle

house = turtle.Turtle()
house.getscreen().bgcolor("Yellow")

house.penup()
house.goto(-200, -200)
house.pendown()


house.fillcolor("lightgreen")
house.begin_fill()

house.forward(500)
house.left(90)
house.forward(300)
house.left(90)
house.forward(500)
house.left(90)
house.forward(300)
house.end_fill()

house.penup()
house.goto(-200, 100)
house.pendown()


house.fillcolor("red")
house.begin_fill()
house.left(-45)
house.backward(200)
house.right(45)
house.backward(215)
house.left(-45)
house.backward(205)
house.end_fill()

house.penup()
house.goto(200, -200)
house.pendown()

house.fillcolor("brown")
house.begin_fill()
house.left(135)
house.backward(140)
house.left(90)
house.backward(60)
house.left(90)
house.backward(140)
house.end_fill()

house.penup()
house.goto(-150, -60)
house.pendown()

house.fillcolor("lightblue")
house.begin_fill()
house.forward(90)
house.right(90)
house.forward(90)
house.right(90)
house.forward(90)
house.right(90)
house.forward(90)
house.end_fill()

house.penup()
house.goto(60, -60)
house.pendown()

house.fillcolor("lightblue")
house.begin_fill()
house.forward(90)
house.right(90)
house.forward(90)
house.right(90)
house.forward(90)
house.right(90)
house.forward(90)
house.end_fill()

turtle.done()