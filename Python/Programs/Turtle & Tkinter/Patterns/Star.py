import turtle

win = turtle.Screen()
win.bgcolor("black")
win.title("Star")
Star = turtle.Turtle()
Star.pencolor("grey")

Star.speed(10)

Star.penup()
Star.goto(-250, 125)
Star.pendown()

Star.fillcolor("yellow")
Star.begin_fill()

for i in range(5):

    Star.forward(500)
    Star.right(144)

Star.end_fill()

turtle.done()