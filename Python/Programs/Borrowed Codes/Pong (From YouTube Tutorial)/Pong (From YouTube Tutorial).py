import turtle
from os import system
import winsound

clear = lambda: system("cls")

clear()

Window = turtle.Screen()
Window.title("Focus on the Game")
Window.bgcolor("black")
Window.setup(800, 600)
Window.tracer(0)

#Score

Score_A = 0
Score_B = 0

#Paddle A

Paddle_A = turtle.Turtle()
Paddle_A.speed(0)
Paddle_A.shape("square")
Paddle_A.color("white")
Paddle_A.shapesize(stretch_wid = 5, stretch_len = 1)
Paddle_A.penup()
Paddle_A.goto(-350, 0)

#Paddle B

Paddle_B = turtle.Turtle()
Paddle_B.speed(0)
Paddle_B.shape("square")
Paddle_B.color("white")
Paddle_B.shapesize(stretch_wid = 5, stretch_len = 1)
Paddle_B.penup()
Paddle_B.goto(350, 0)

#Ball

Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)

#dx, d = Delta or Change

Ball.dx = 0.3
Ball.dy = 0.3

#Pen

Pen = turtle.Turtle()
Pen.speed(0)
Pen.color("white")
Pen.penup()
Pen.hideturtle()
Pen.goto(0, 260)
Pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))

#Function

def Paddle_A_Up():

    y = Paddle_A.ycor()
    y += 20
    Paddle_A.sety(y)

def Paddle_A_Down():

    y = Paddle_A.ycor()
    y -= 20
    Paddle_A.sety(y)

def Paddle_B_Up():

    y = Paddle_B.ycor()
    y += 20
    Paddle_B.sety(y)

def Paddle_B_Down():

    y = Paddle_B.ycor()
    y -= 20
    Paddle_B.sety(y)

Window.listen()
Window.onkeypress(Paddle_A_Up, 'w')
Window.onkeypress(Paddle_A_Down, 's')
Window.onkeypress(Paddle_B_Up, 'Up')
Window.onkeypress(Paddle_B_Down, 'Down')

#Main Game Loop

while True:
    
    Window.update()

    #Move the Ball

    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Border Checking

    if Ball.ycor() > 290:

        Ball.sety(290)
        Ball.dy *= -1
        winsound.PlaySound(f"{__file__.removesuffix('Pong (From YouTube Tutorial).py')}bounce.wav", winsound.SND_ASYNC)

    if Ball.ycor() < -290:

        Ball.sety(-290)
        Ball.dy *= -1
        winsound.PlaySound(f"{__file__.removesuffix('Pong (From YouTube Tutorial).py')}bounce.wav", winsound.SND_ASYNC)

    if Ball.xcor() > 390:

        Ball.goto(0, 0)
        Ball.dx *= -1
        Score_A += 1
        Pen.clear()
        Pen.write(f"Player A: {Score_A} Player B: {Score_B}", align = "center", font = ("Courier", 24, "normal"))

    if Ball.xcor() < -390:

        Ball.goto(0, 0)
        Ball.dx *= -1
        Score_B += 1
        Pen.clear()
        Pen.write(f"Player A: {Score_A} Player B: {Score_B}", align = "center", font = ("Courier", 24, "normal"))

    #Paddle and Ball Collisions
    
    if Ball.xcor() > 340 and Ball.xcor() < 350 and Ball.ycor() < Paddle_B.ycor() + 50 and Ball.ycor() > Paddle_B.ycor() - 50:
        
        Ball.setx(340)
        Ball.dx *= -1
        winsound.PlaySound(f"{__file__.removesuffix('Pong (From YouTube Tutorial).py')}bounce.wav", winsound.SND_ASYNC)

    if Ball.xcor() < -340 and Ball.xcor() > -350 and Ball.ycor() < Paddle_A.ycor() + 50 and Ball.ycor() > Paddle_A.ycor() - 50:
        
        Ball.setx(-340)
        Ball.dx *= -1
        winsound.PlaySound(f"{__file__.removesuffix('Pong (From YouTube Tutorial).py')}bounce.wav", winsound.SND_ASYNC)