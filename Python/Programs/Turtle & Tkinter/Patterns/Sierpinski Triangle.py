from turtle import Screen, Turtle, done
import random

win = Screen()
win.title("Sierpinski Triangle")
win.tracer(0)

def triangle_size(size, centre):

    global _1, _2, _3

    win.screensize(size+100, size+100)

    _1 = Turtle()
    _1.ht()
    _1.pensize(2)
    _1.speed(0)
    _1.pu()

    _1.goto(centre)
    _1.sety(size/2)

    _2 = _1.clone()
    _2.seth(-120)
    _2.fd(size)

    _3 = _1.clone()
    _3.seth(-60)
    _3.fd(size)

    _1.dot()
    _2.dot()
    _3.dot()

def sierpinski_triangle(quick, times = -1):

    choices = [_1, _2, _3]

    drawer = Turtle()
    drawer.pensize(-1)
    drawer.speed(0)
    drawer.pu()
    drawer.ht()

    choice1 = choice2 = None

    while choice1 == choice2:

        choice1 = choices[random.randint(0, 2)]
        choice2 = choices[random.randint(0, 2)]

    drawer.setx((choice1.xcor()+choice2.xcor())/2)
    drawer.sety((choice1.ycor()+choice2.ycor())/2)

    drawer.dot()

    while times:
        
        choice = choices[random.randint(0, 2)]

        drawer.setx((choice.xcor()+drawer.xcor())/2)
        drawer.sety((choice.ycor()+drawer.ycor())/2)

        drawer.dot()

        if quick:
            if times%5000 == 0: win.update()
        else: win.update()

        times -= 1

triangle_size(500, (0, 0))
sierpinski_triangle(True, 50000)

done()
