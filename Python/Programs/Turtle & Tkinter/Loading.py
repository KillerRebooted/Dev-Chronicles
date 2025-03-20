from turtle import *

win = Screen()
win.title("Loading")
win.bgcolor("white")

Circle = Turtle()
Circle_Erase = Turtle()

Circle.hideturtle()
Circle_Erase.hideturtle()

Circle.pencolor("black")
Circle_Erase.pencolor("white")

Circle.pensize(20)
Circle_Erase.pensize(20)

Circle.shape("square")
Circle_Erase.shape("square")

while True:

    Circle.circle(50)
    Circle_Erase.circle(50)

    Circle.clear()
    Circle_Erase.clear()