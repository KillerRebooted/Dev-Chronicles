from turtle import *
from calibrate import x_offset, y_offset
import threading, time

win = Screen()
win.title("Stalker")
win.tracer(0)

TurtleScreen._RUNNING=True

def mouse_loc(event):
    global x_offset, y_offset, first

    shadow.goto(event.x-x_offset, -event.y+y_offset)
    if first:
        t1.start()
        first = False

def follow():
    
    stalker.pd()
    clear.pd()
    
    while True:
        
        prev_turn = stalker.heading()
        stalker.seth(stalker.towards(shadow.pos()))
        
        if abs(prev_turn-stalker.heading()) == 180:
            stalker.pu()
            stalker.goto(0, 0)
            stalker.pencolor("black")
            stalker.write("GAME OVER", font=("Courier", 40, "bold"), align="center")
            break

        stalker.fd(10)
        coords.append((stalker.xcor(), stalker.ycor()))
        if len(coords) > 100:
            clear.goto(coords.pop(0))
        time.sleep(0.01)
        win.update()

stalker = Turtle()
stalker.pensize(4)
stalker.pencolor("red")
stalker.pu()
stalker.ht()
stalker.speed(0)
coords = []

shadow = stalker.clone()
shadow.pencolor("green")
shadow.pu()
shadow.ht()

clear = stalker.clone()
clear.pencolor("white")

canvas = win.getcanvas()
canvas.bind("<Motion>", mouse_loc)

t1 = threading.Thread(target=follow)
first=True

done()