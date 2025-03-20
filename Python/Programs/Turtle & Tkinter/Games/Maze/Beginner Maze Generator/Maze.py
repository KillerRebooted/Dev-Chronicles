import turtle
import random

win = turtle.Screen()
win.bgcolor("white")
win.title("Maze")

Maze = turtle.Turtle()
Walls = turtle.Turtle()
Player = turtle.Turtle()

image = f"{__file__.removesuffix('Maze.py')}Mario.gif"
win.register_shape(image)
Player.shape(image)
Player.penup()
Player.hideturtle()

Maze.hideturtle()
Walls.hideturtle()

Maze.speed(10)
Walls.speed(10)

def move_up():

    Player.setheading(90)
    Player.forward(10)

def move_down():

    Player.setheading(-90)
    Player.forward(10)

def move_left():

    Player.setheading(180)
    Player.forward(10)

def move_right():

    Player.setheading(0)
    Player.forward(10)

x, y, z = -250, 250, 460
forward = 560

for i in range(3):
    
    Start = random.randint(0, z)
    End = random.randint(0, z)

    if forward == 560:
        Start_Pos = -250+End+15

    z -= 60

    Maze.penup()
    
    Maze.goto(x, y)
    x += 30
    y -= 30

    Maze.pendown()

    open = "start"
    forward -= 60

    for i in range(2):

        Maze.forward(forward)
        Maze.right(90)

        if open == "start":

            Maze.forward(Start)
            Maze.penup()
            Maze.forward(30)
            Maze.pendown()
            Maze.forward(forward-Start-30)
            Maze.right(90)

            open = "end"

        else:

            Maze.forward(End)
            Maze.penup()
            Maze.forward(30)
            Maze.pendown()
            Maze.forward(forward-End-30)
            Maze.right(90)

Maze.penup()

#Left or Right
LR = random.choice("LRLRLRLR")

if LR == "L":
    Maze.goto(-160, 160)

else:
    Maze.goto(160, 160)

Maze.pendown()
forward = random.randint(100, 230)

#Square 1

Start = random.randint(0, forward-30)
End = random.randint(0, forward-30)

if LR == "L":
    Maze.forward(forward)
    Maze.right(90)
        
    Maze.forward(Start)
    Maze.penup()
    Maze.forward(30)
    Maze.pendown()
    Maze.forward(forward-Start-30)

    Maze.right(90)
    Maze.forward(forward)
    Maze.right(90)
        
    Maze.forward(End)
    Maze.penup()
    Maze.forward(30)
    Maze.pendown()
    Maze.forward(forward-End-30)

else:
    Maze.forward(-forward)
    Maze.right(90)
        
    Maze.forward(Start)
    Maze.penup()
    Maze.forward(30)
    Maze.pendown()
    Maze.forward(forward-Start-30)

    Maze.left(90)
    Maze.forward(forward)
    Maze.left(90)
        
    Maze.forward(End)
    Maze.penup()
    Maze.forward(30)
    Maze.pendown()
    Maze.forward(forward-End-30)

forward2 = (290-forward)

#Square 2

Opening = random.randint(0, forward2-30)

if LR == "L":
    Maze.penup()
    Maze.goto(-160, 130-forward)
    Maze.right(90)

    Maze.pendown()

    Maze.forward(forward)
    Maze.right(90)
        
    Maze.forward(Opening)
    Maze.penup()
    Maze.forward(30)
    Maze.pendown()
    Maze.forward(forward2-Opening-30)

    Maze.right(90)
    Maze.forward(forward)
    Maze.right(90)
        
    Maze.forward(forward2)

else:
    Maze.penup()
    Maze.goto(160, 130-forward)
    Maze.right(90)

    Maze.pendown()

    Maze.forward(-forward)
    Maze.right(90)
        
    Maze.forward(Opening)
    Maze.penup()
    Maze.forward(30)
    Maze.pendown()
    Maze.forward(forward2-Opening-30)

    Maze.left(90)
    Maze.forward(forward)
    Maze.left(90)
        
    Maze.forward(forward2)

#Sqaure 3

Opening = random.randint(0, 290)

if LR == "L":

    Maze.penup()
    Maze.goto(-130+forward, 160)
    Maze.right(90)
    Maze.pendown()

    Maze.forward(290-forward)
    Maze.right(90)

    Maze.forward(Opening)
    Maze.penup()
    Maze.forward(30)
    Maze.pendown()
    Maze.forward(290-Opening)

    Maze.right(90)
    Maze.forward(290-forward)
    Maze.right(90)
    Maze.forward(320)

else:

    Maze.penup()
    Maze.goto(-160, 160)
    Maze.right(90)
    Maze.pendown()

    Maze.forward(290-forward)
    Maze.right(90)

    Maze.forward(Opening)
    Maze.penup()
    Maze.forward(30)
    Maze.pendown()
    Maze.forward(290-Opening)

    Maze.right(90)
    Maze.forward(290-forward)
    Maze.right(90)
    Maze.forward(320)

#Outer Walls

x, y = -220, 220

for i in range(2):

    Walls.penup()

    Wall_X = random.randint(x, y)
    Wall_Y = [220, 190]

    Walls.goto(Wall_X, Wall_Y[i])
    Walls.pendown()
    Walls.setheading(90)
    Walls.forward(30)

    Walls.penup()
    Wall_X = random.randint(x, y)
    
    Walls.goto(Wall_X, -Wall_Y[i])
    Walls.pendown()
    Walls.setheading(270)
    Walls.forward(30)

    x += 60
    y -= 60

#Inner Walls

if LR == "L":    
    
    for i in range (3):

        Walls.penup()
        x, y = -160, -160+forward

        Wall_X = random.randint(x, y)
        Wall_Y = [190, 160-forward, 130-forward-forward2]

        Walls.goto(Wall_X, Wall_Y[i])
        Walls.pendown()
        Walls.forward(30)

    Walls.penup()
    x, y = -130+forward, 160

    Wall_X = random.randint(x, y)
    Wall_Y = random.choice([190, -160, 190, -160, 190, -160])

    Walls.goto(Wall_X, Wall_Y)
    Walls.pendown()
    Walls.forward(30)

else:

    for i in range (3):

        Walls.penup()
        x, y = 160-forward, 160

        Wall_X = random.randint(x, y)
        Wall_Y = [190, 160-forward, 130-forward-forward2]

        Walls.goto(Wall_X, Wall_Y[i])
        Walls.pendown()
        Walls.forward(30)

    Walls.penup()
    x, y = -160, 130-forward

    Wall_X = random.randint(x, y)
    Wall_Y = random.choice([190, -160, 190, -160, 190, -160])

    Walls.goto(Wall_X, Wall_Y)
    Walls.pendown()
    Walls.forward(30)

Player.goto(-290, Start_Pos)
Player.showturtle()

win.onkeypress(move_up, "w")
win.onkeypress(move_down, "s")
win.onkeypress(move_left, "a")
win.onkeypress(move_right, "d")

win.listen()

turtle.mainloop()