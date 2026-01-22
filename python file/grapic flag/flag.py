import turtle

from sympy import FallingFactorial

flag = turtle.Turtle()
flag.getscreen().bgcolor("Skyblue")
# flag.speed(10)

flag.penup()
flag.goto(0,-270)
flag.pendown()

#stage 1
flag.color("saddle brown")
flag.fillcolor("saddle brown")
flag.begin_fill()
flag.backward(300)
flag.forward(600)
flag.left(90)
flag.forward(70)
flag.left(90)
flag.forward(600)
flag.left(90)
flag.forward(70)
flag.end_fill()

flag.penup()
flag.goto(0,-200)
flag.pendown()

#stage 2
flag.color("sandy brown")
flag.fillcolor("sandy brown")
flag.begin_fill()
flag.left(90)
flag.forward(200)
flag.left(90)
flag.forward(70)
flag.left(90)
flag.forward(400)
flag.left(90)
flag.forward(70)
flag.left(90)
flag.forward(200)
flag.end_fill()

flag.penup()
flag.goto(0,-130)
flag.pendown()

#stage 3
flag.color("indian red")
flag.fillcolor("indian red")
flag.begin_fill()
flag.forward(100)
flag.left(90)
flag.forward(70)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.forward(70)
flag.left(90)
flag.forward(100)
flag.end_fill()

flag.penup()
flag.goto(-30,-60)
flag.pendown()

#flag stick
flag.color("brown4")
flag.fillcolor("brown4")
flag.begin_fill()
flag.left(90)
flag.forward(400)
flag.left(-90)
flag.forward(20)
flag.left(270)
flag.forward(400)
flag.left(-90)
flag.forward(30)
flag.end_fill()

flag.penup()
flag.goto(-10,320)
flag.pendown()

#flag p1 orange
flag.color("black")
flag.fillcolor("#FF671F")
flag.begin_fill()
flag.left(180)
flag.forward(240)
flag.left(-90)
flag.forward(50)
flag.left(-90)
flag.forward(240)
flag.left(-90)
flag.forward(50)
flag.end_fill()

flag.penup()
flag.goto(-10,270)
flag.pendown()

#flag p2 white
flag.color("black")
flag.fillcolor("#FFFFFF")
flag.begin_fill()
flag.left(-90)
flag.forward(240)
flag.left(-90)
flag.forward(50)
flag.left(-90)
flag.forward(240)
flag.left(-90)
flag.forward(50)
flag.end_fill()

flag.penup()
flag.goto(-10,220)
flag.pendown()

#flag p3 green
flag.color("black")
flag.fillcolor("#046A38")
flag.begin_fill()
flag.left(-90)
flag.forward(240)
flag.left(-90)
flag.forward(50)
flag.left(-90)
flag.forward(240)
flag.left(-90)
flag.forward(50)
flag.end_fill()

flag.penup()
flag.goto(125,245)
flag.pendown()

#ashok chaker
flag.color("black")
flag.fillcolor("#06038D")
flag.begin_fill()
flag.circle(17)
flag.end_fill()

flag.penup()
flag.goto(-250,290)
flag.pendown()

#sun
flag.speed(20)
flag.color("#FFE484")
flag.fillcolor("#FFCC33")

for i in range(30):
    flag.begin_fill()
    flag.left(90)
    flag.forward(100)
    flag.left(120)
    flag.forward(100)
    flag.left(120)
    flag.forward(100)
    flag.end_fill()

flag.penup()
flag.goto(-320,-300)
flag.pendown()

#hang
flag.color("black")
flag.fillcolor("#F9F6EE")
flag.begin_fill()
flag.left(90)
flag.forward(640)
flag.left(-90)
flag.forward(65)
flag.left(-90)
flag.forward(640)
flag.left(-90)
flag.forward(65)
flag.end_fill()

flag.penup()
flag.goto(-300,-350)
flag.pendown()

#write
flag.color("#6F8FAF")
flag.write("HAPPY INDEPENDENCE DAY!!!", font=("arial", 40, "bold"))

turtle.done()

