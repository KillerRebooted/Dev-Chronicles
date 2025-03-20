from turtle import *

win = Screen()
win.title("Spider Web")
win.bgcolor("black")

Spider_Web = Turtle()
Spider_Web.pencolor("white")
Spider_Web.width(2)
Spider_Web.speed(0)

for i in range(360):

    Spider_Web.fd(i)
    Spider_Web.right(60)

    if i%50 == 0:

        for j in range(60, 361, 60):    
            
            Spider_Web.penup()
            Spider_Web.goto(0, 0)
            Spider_Web.setheading(j)
            Spider_Web.pendown()
            Spider_Web.fd(i)

        Spider_Web.right(120)

done()