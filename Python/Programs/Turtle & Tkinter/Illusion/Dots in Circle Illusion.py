from turtle import *
import time
import keyboard

win = Screen()
win.title("Illusion")
win.tracer(0.1)

def balls(particle_num, clone_size, radius, ref_circle):

    ref_turt = Turtle("circle")
    ref_turt.shapesize(clone_size, clone_size)

    if ref_circle:
        ref_turt.pu()
        ref_turt.seth(-90)
        ref_turt.fd(radius)
        ref_turt.seth(0)
        ref_turt.pd()
        ref_turt.circle(radius)

    ref_turt.pu()
    ref_turt.goto(0, 0)
    ref_turt.ht()

    clones = []
    for cl in range(particle_num):
        clone = ref_turt.clone()
        clone.st()
        clones.append(clone)

    return (ref_turt, clones)

def df(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

radius = 150
center, particles = balls(10, 0.5, radius, True)

center.goto(radius/2, 0)
center.seth(90)

start_pos = ()
pendown = False

while True:

    center.circle(radius/2, 1)

    heading = center.heading()
    for particle in particles:
        particle.ht()
        particle.goto(center.pos())
        particle.seth(-heading)
        particle.fd(radius/2)
        particle.st()

        if pendown:
            particle.dot(3)

        heading += 360/len(particles)

    if tuple(round(i, 2) for i in center.pos()) == start_pos:
        pendown = False

    if keyboard.is_pressed("s"):
        
        if not pendown:
            pendown = True
            start_pos = tuple(round(i, 2) for i in center.pos())
        else:
            for particle in particles:
                particle.clear()
            cur_pos = center.pos()
            cur_head = center.heading()

            center.goto(0, 0)
            center.seth(-90)
            center.fd(radius)
            center.seth(0)
            center.pd()
            center.circle(radius)
            center.pu()

            center.goto(cur_pos)
            center.seth(cur_head)

            pendown = False

    time.sleep(0.01)
    win.update()