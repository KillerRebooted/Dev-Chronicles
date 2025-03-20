from turtle import *
import math

win = Screen()
win.title("Bulb")
win.tracer(0)
win.colormode(255)

bulb = Turtle()
bulb.pu()
bulb.pensize(5)
bulb.speed(0)
bulb.ht()

slider = Turtle("circle")
slider.speed(0)
slider.pensize(5)
slider.pu()

def draw_bulb(size, fill=False, brightness=1):

    global half_circumference
    
    #Top of Bulb

    bulb.goto(size, 0)
    bulb.seth(90)

    bulb.pd()

    if fill:
        bulb.clear()
        color = (255, 255, int((1-brightness)*255))
        bulb.fillcolor(color)
        bulb.begin_fill()
    
    half_circumference = math.pi*size
    
    bulb.fd(half_circumference/180)
    for i in range(180):
        bulb.left(1)
        bulb.fd(half_circumference/180)

    #Bottom Half

    fourth_circumference = half_circumference/2

    side = 1
    for i in range(2):

        bulb.fd(fourth_circumference/180)
        
        for i in range(90):
            bulb.left(1*side)
            bulb.fd(fourth_circumference/180)

        for i in range(90):
            bulb.right(1*side)
            bulb.fd(fourth_circumference/180)

        bulb.seth(90)

        side *= -1

    #Base

    bulb.pu()
    bulb.goto(-size/3.5, -size/1.8)
    bulb.seth(0)
    bulb.pd()

    if fill:
        bulb.end_fill()

    bulb.fillcolor("brown")
    bulb.begin_fill()

    sides = [size/1.75, size]
    for i in range(4):
        bulb.fd(sides[i%2])
        bulb.right(90)

    bulb.end_fill()

    win.update()

def draw_slider(size_circle, size_slider):

    slider.goto(size_circle+200, 0)

    slider.seth(90)
    slider.pd()

    slider.fd(size_slider)
    slider.fd(-2*size_slider)

def value_update(x, y):

    global brightness

    if (y <= size_slider) and (y >= -size_slider):
        slider.sety(y)

    brightness = (slider.ycor()+size_slider)/(2*size_slider)

    bulb.pu()
    draw_bulb(size_circle, True, brightness)
    
    win.update()

size_circle = 200
size_slider = 100

win.screensize(size_circle+2000, size_circle+2000)

draw_bulb(size_circle)
draw_slider(size_circle, size_slider)

slider.ondrag(value_update)

win.update()

done()