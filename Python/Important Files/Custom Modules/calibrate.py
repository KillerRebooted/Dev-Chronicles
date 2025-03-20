from turtle import *

win1 = Screen()
win1.title("Callibrate")

def calibrate(mx, my):
    global x_offset, y_offset

    x_offset = abs(mx-x) 
    y_offset = abs(my-y)

    bye()

def mouse_coords(event):
    global x, y

    x = event.x
    y = -event.y

canvas = win1.getcanvas()

win1.onscreenclick(calibrate, 1)
canvas.bind("<Motion>", mouse_coords)

done()