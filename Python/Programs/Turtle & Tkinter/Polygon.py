import turtle

sides = int(input("Enter the Number of Sides: "))

win = turtle.Screen()
win.bgcolor("white")
win.title("Polygon")
win.tracer(0)

Polygon = turtle.Turtle()

Polygon.penup()

if sides <= 6:
    Polygon.goto(-500/sides, 500/sides)

elif (sides >= 7) and (sides <= 10):
    Polygon.goto(-500/sides, 200)

else:
    Polygon.goto(0, 200)

Polygon.pendown()

Polygon.fillcolor("yellow")
Polygon.begin_fill()

for i in range(sides):

    Polygon.forward(1000/sides)
    Polygon.right(360/sides)

    win.update()

Polygon.end_fill()

turtle.done()