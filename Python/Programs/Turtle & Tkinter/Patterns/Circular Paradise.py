from turtle import *

win = Screen()
win.title("Circular Paradise")
win.bgcolor("white")

Circle = Turtle()
Circle.speed(0)

num = 10

for i in range(100):

    Circle.circle(num)
    Circle.circle(-num)
    Circle.right(10)

    num += 1

done()