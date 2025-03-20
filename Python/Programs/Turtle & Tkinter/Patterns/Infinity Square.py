import turtle

win = turtle.Screen()
win.bgcolor("light green")
win.title("Infinity Square")
Infinity_Square = turtle.Turtle()

Infinity_Square.speed(0)
Infinity_Square.penup()
Infinity_Square.goto(-250, 250)
Infinity_Square.pendown()

for i in range(500, 0, -3):

    Infinity_Square.forward(i)
    Infinity_Square.right(90)

turtle.done()