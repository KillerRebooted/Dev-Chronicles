from turtle import *

win = Screen()
win.title("Cube")
win.bgcolor("white")

Cube = Turtle()
Cube.width(2)
Cube.penup()

Cube.goto(-50, 50)
Cube.pendown()

Cube.fd(100)
Cube.right(90)
Cube.fd(100)
Cube.right(90)
Cube.fd(100)
Cube.right(90)
Cube.fd(100)

Cube.penup()
Cube.goto(-30, 80)
Cube.pendown()

Cube.right(90)
Cube.fd(100)
Cube.right(90)
Cube.fd(100)
Cube.right(90)
Cube.fd(100)
Cube.right(90)
Cube.fd(100)

Cube.penup()

Cube.goto(-30, 80)
Cube.pendown()
Cube.goto(-50, 50)

Cube.penup()

Cube.goto(70, 80)
Cube.pendown()
Cube.goto(50, 50)

Cube.penup()

Cube.goto(70, -20)
Cube.pendown()
Cube.goto(50, -50)

Cube.penup()

Cube.goto(-30, -20)
Cube.pendown()
Cube.goto(-50, -50)

done()