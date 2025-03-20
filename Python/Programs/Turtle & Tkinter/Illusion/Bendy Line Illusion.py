from turtle import *

win = Screen()
win.title("Bendy Line Illusion")
win.bgcolor("black")

Illusion = Turtle()
Illusion.pencolor("white")
Illusion.width(1.5)
Illusion.speed(0)

Illusion.hideturtle()

Colors = ["red", "blue"]

x = 0

for i in range(250, -250, -25):

    Illusion.penup()

    Illusion.goto(-250, i)
    Illusion.pendown()

    x += 1

    Illusion.pencolor(Colors[x%2])

    Illusion.goto(250, -i)

Illusion.pencolor("white")
Illusion.penup()

Illusion.goto(-250, 25)
Illusion.pendown()
Illusion.goto(250, 25)

Illusion.penup()

Illusion.goto(-250, -25)
Illusion.pendown()
Illusion.goto(250, -25)

done()