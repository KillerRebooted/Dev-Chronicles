from turtle import Screen, Turtle, bye, done, mainloop, TurtleScreen
from calibrate import x_offset, y_offset

win = Screen()
win.title("Turtle Paint")
win.colormode(255)
win.tracer(0)

TurtleScreen._RUNNING=True

painter = Turtle()
painter.pensize(4)
painter.shapesize(0.01, 0.01)
painter.speed(0)
painter.pu()

rainbow_pen = Turtle("square")
rainbow_pen.pu()
rainbow_pen.goto(300, -285)
rainbow_pen.write("Rainbow Pen", align="center" , font=("Arial", 14, "bold"))
rainbow_pen.goto(300, -250)

win.update()

r = 255
g = 0
b = 0

step_color = 15

def paint(event):

    global r, g, b
    
    painter.goto(event.x-x_offset, -event.y+y_offset)

    if rainbow_boolean:
        painter.color((r, g, b))
        rainbow_pen.color((r, g, b))
    else:
        painter.color("black")
        rainbow_pen.color("black")

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
        
    win.update()

def rainbow_toggle(boolean):
    global rainbow_boolean

    if boolean:
        rainbow_boolean = False
    else:
        rainbow_boolean = True

canv = win.getcanvas()
canv.bind("<Motion>", paint)

def draw(x, y):
    painter.pd()
    painter.dot(6)
def stop(x, y):
    painter.pu()

painter.onclick(draw)
painter.onrelease(stop)

rainbow_boolean = True
rainbow_pen.onclick(lambda x, y: rainbow_toggle(rainbow_boolean))

win.listen()

win.onkeypress(bye, "Escape")

done()
mainloop()
