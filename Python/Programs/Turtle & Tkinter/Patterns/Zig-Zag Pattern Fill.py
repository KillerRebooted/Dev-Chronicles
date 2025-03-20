from turtle import *
from time import sleep

win = Screen()
win.title("Zig-Zag Pattern Fill")
win.colormode(255)
win.tracer(0)

pattern = Turtle()
pattern.speed(0)
pattern.pensize(4)
pattern.pu()
pattern.ht()

square = Turtle("square")
square.pensize(3)
square.shapesize(1, 1)
square.pu()

counter = Turtle()
counter.ht()
counter.pu()

def make_square():
    global corner_x, corner_y

    square.goto(-size, size/2)
    square.pd()

    for i in range(4):
        square.fd(size*2 if i%2==0 else size)
        square.right(90)

    corner_x = [-size, size]
    corner_y = [-size/2, size/2]

    square.pu()

    win.update()

def make_design():
    pattern.goto(-size, -size/2)
    pattern.pd()

    dy = 1
    dx = (size*2) / ((size-size/4.5)/dy)

    move = (dx**2 + dy**2)**0.5

    num = 0
    hits = 0
    while True:

        pattern.seth(pattern.towards(pattern.xcor()+dx, pattern.ycor()+dy))
        pattern.fd(move)
        square.goto(pattern.pos())

        if not (corner_x[0] < pattern.xcor() < corner_x[1]):
            dx *= -1
            hits += 1
            count("x")
        if not (corner_y[0] < pattern.ycor() < corner_y[1]):
            dy *= -1
            hits += 1
            count("y")

        if hits == 118:
            done()

        win.update()
        num += 1

        sleep(0.005)

def count(hit):
    global hit_x, hit_y

    if hit == "x":
        hit_x += 1
    elif hit == "y":
        hit_y += 1

    counter.clear()
    counter.write(f"Top/Bottom Hits : {hit_y}    Left/Right Hits : {hit_x}", font=("Courier", 24, "bold"), align="center")

    win.update()

size = 400

hit_x, hit_y = 0, 0

counter.sety(3*size/4)
counter.write(f"Top/Bottom Hits : {hit_y}    Left/Right Hits : {hit_x}", font=("Courier", 24, "bold"), align="center")

make_square()
make_design()

done()