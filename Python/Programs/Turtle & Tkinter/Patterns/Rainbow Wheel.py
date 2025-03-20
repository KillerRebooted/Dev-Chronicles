from turtle import *

win = Screen()
win.colormode(255)
win.title("Rainbow Wheel")
win.tracer(0)

turtle = Turtle()
turtle.pensize(2)
turtle.speed(0)
turtle.pencolor(255, 0, 0)

r = 255
g = 0
b = 0

step_color = 1

size = 250

for i in range(255*6):
    
    turtle.fd(size)
    turtle.fd(-size)

    if (r == 255) and (g != 255) and (b == 0):
        g += step_color
    elif (r != 0) and (g == 255) and (b == 0):
        r -= step_color
    elif (r == 0) and (g == 255) and (b != 255):
        b += step_color
    elif (r == 0) and (g != 0) and (b == 255):
        g -= step_color
    elif (r != 255) and (g == 0) and (b == 255):
        r += step_color
    elif (r == 255) and (g == 0) and (b != 0):
        b -= step_color
    
    turtle.pencolor((r, g, b))
    
    turtle.left(360 / (255*6))

    win.update()

def visibility():

    if turtle.isvisible(): turtle.ht()
    else: turtle.st()

    win.update()

win.onkeypress(visibility, "h")
win.listen()

done()