from turtle import *
import random, math, time, os

win = Screen()
win.title(os.path.basename(__file__)[:-3])
win.tracer(0)

def wave_function(boundary_size, longitudinal, particle_amount, wave_type, A, T, lam):

    boundary_creator = Turtle()
    boundary_creator.ht()
    boundary_creator.pensize(4)
    boundary_creator.pu()

    if longitudinal:

        width = 2*boundary_size + 2*A
        height = boundary_size/2

    else:

        width = 2*boundary_size
        height = 5*A

    boundary_creator.setx(-width/2)
    boundary_creator.sety(height/2)

    boundary_creator.pd()

    for i in range(2):
        boundary_creator.fd(width)
        boundary_creator.right(90)
        boundary_creator.fd(height)
        boundary_creator.right(90)

    particle_tracer = Turtle()
    particle_tracer.seth(90)
    particle_tracer.color("red")
    particle_tracer.pu()

    particles = []
    for i in range(particle_amount):
        particle = Turtle("circle")
        particle.shapesize(.3, .3)
        particle.pu()
        
        if longitudinal:
            particle.setpos(random.randint(-boundary_size, boundary_size), random.randint(int(-height//2), int(height//2)) )
        else:
            particle.setx(-boundary_size + (boundary_size/particle_amount)*2*i)

        particles.append(particle)

    og_coords = [particle.pos() for particle in particles]

    start = time.time()

    chosen_one = random.randint(0, particle_amount-1)

    particles[chosen_one].color("red")
    particles[chosen_one].shapesize(.4, .4)
    particle_tracer.setx(particles[chosen_one].xcor())

    def make_wave(wave_type, A, T, lam):

        t = time.time()-start

        for index, particle in enumerate(particles):

            x = int(particle.xcor()+width/2)

            if wave_type == "progressive": y = "A*math.sin( ((2*math.pi)/T)*t - ((2*math.pi)/lam)*x)"
            elif wave_type == "standing": y = "A*math.sin(((2*math.pi)/lam)*x)*math.cos(((2*math.pi)/T)*t)"

            if longitudinal:
                particle.setx(og_coords[index][0] + eval(y))
            else:
                particle.sety(eval(y))

        particle_tracer.setpos(particles[chosen_one].xcor(), particles[chosen_one].ycor() - 20)

        win.update()

    win.listen()
    win.onkeypress(win.bye, "Escape")

    while True:
        make_wave(wave_type, A, T, lam)

if __name__ == "__main__":
    wave_function(boundary_size=300, longitudinal=False, particle_amount=1000, wave_type="progressive", A=80, T=3, lam=100)