from turtle import *
import math

size = 3
less_updates = True

def next_prime(n):
    while True:
        n += 1
        for i in range(2, int(math.sqrt(n)+1)):
            if n%i == 0:
                break
        else:
            break
    return n

def draw_square_dot(t, size):
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.fd(size)
        t.left(90)
    t.end_fill()
    t.penup()

win = Screen()
win.title("Bulb")
win.tracer(0)

spiral = Turtle()
spiral.speed(0)
spiral.pu()
spiral.ht()
spiral.goto(0, 0)

req_steps = 0
cur_steps = 0
grid = 1
prime = next_prime(1)

while True:

    if grid == prime:
        draw_square_dot(spiral, size)
        prime = next_prime(prime)
        if not less_updates:
            win.update()

    if cur_steps == req_steps:
        req_steps += 2
        cur_steps = 0
        spiral.left(90)
        if less_updates:
            win.update()

    spiral.fd(size)
    grid += 1
    cur_steps += 1
    
    if cur_steps == req_steps/2:
        spiral.left(90)
        if less_updates:
            win.update()