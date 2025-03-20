from turtle import *

win = Screen()
win.title("Rubiks Cube")
win.bgcolor("black")

Rubiks_Cube_Green = Turtle()
Rubiks_Cube_Green.width(2)
Rubiks_Cube_Green.pencolor("black")
Rubiks_Cube_Green.speed(10)
Rubiks_Cube_Green.hideturtle()
Rubiks_Cube_Green.penup()

Rubiks_Cube_White = Turtle()
Rubiks_Cube_White.width(2)
Rubiks_Cube_White.pencolor("black")
Rubiks_Cube_White.speed(10)
Rubiks_Cube_White.hideturtle()
Rubiks_Cube_White.penup()

Rubiks_Cube_Red = Turtle()
Rubiks_Cube_Red.width(2)
Rubiks_Cube_Red.pencolor("black")
Rubiks_Cube_Red.speed(10)
Rubiks_Cube_Red.hideturtle()
Rubiks_Cube_Red.penup()

Rubiks_Cube_Green.goto(-100, 100)
Rubiks_Cube_Green.pendown()

Rubiks_Cube_White.goto(-100, 100)
Rubiks_Cube_White.pendown()

Rubiks_Cube_Red.goto(100, -100)
Rubiks_Cube_Red.pendown()

def Cube(Color, s1, a1, s2, a2, s3, a3, s4, a4):

    if Color == "Green":

        Rubiks_Cube_Green.fillcolor("green")
        Rubiks_Cube_Green.begin_fill()
        
        Rubiks_Cube_Green.setheading(0)

        Rubiks_Cube_Green.fd(s1)
        Rubiks_Cube_Green.right(a1)

        Rubiks_Cube_Green.fd(s2)
        Rubiks_Cube_Green.right(a2)

        Rubiks_Cube_Green.fd(s3)
        Rubiks_Cube_Green.right(a3)

        Rubiks_Cube_Green.fd(s4)
        Rubiks_Cube_Green.right(a4)

        Rubiks_Cube_Green.end_fill()

        Rubiks_Cube_Green.fd(s1/3)
        Rubiks_Cube_Green.right(a1)
        Rubiks_Cube_Green.fd(s2)
        Rubiks_Cube_Green.left(a3)
        Rubiks_Cube_Green.fd(s3/3)
        Rubiks_Cube_Green.left(a2)
        Rubiks_Cube_Green.fd(s2)

        Rubiks_Cube_Green.right(a4)
        Rubiks_Cube_Green.fd(s1/3)
        Rubiks_Cube_Green.right(a1)
        Rubiks_Cube_Green.fd(s2/3)
        Rubiks_Cube_Green.right(a2)
        Rubiks_Cube_Green.fd(s1)
        Rubiks_Cube_Green.left(180-a3)
        Rubiks_Cube_Green.fd(s4/3)
        Rubiks_Cube_Green.left(180-a2)
        Rubiks_Cube_Green.fd(s1)

    if Color == "White":
        
        Rubiks_Cube_White.fillcolor("white")
        Rubiks_Cube_White.begin_fill()

        Rubiks_Cube_White.setheading(45)

        Rubiks_Cube_White.fd(s1)
        Rubiks_Cube_White.right(a1)

        Rubiks_Cube_White.fd(s2)
        Rubiks_Cube_White.right(a2)

        Rubiks_Cube_White.fd(s3)
        Rubiks_Cube_White.right(a3)

        Rubiks_Cube_White.fd(s4)
        Rubiks_Cube_White.right(a4)

        Rubiks_Cube_White.end_fill()

        Rubiks_Cube_White.fd(s1/3)
        Rubiks_Cube_White.right(a1)
        Rubiks_Cube_White.fd(s2)
        Rubiks_Cube_White.left(a3)
        Rubiks_Cube_White.fd(s3/3)
        Rubiks_Cube_White.left(a2)
        Rubiks_Cube_White.fd(s2)

        Rubiks_Cube_White.right(a4)
        Rubiks_Cube_White.fd(s1/3)
        Rubiks_Cube_White.right(a1)
        Rubiks_Cube_White.fd(s2/3)
        Rubiks_Cube_White.right(a2)
        Rubiks_Cube_White.fd(s1)
        Rubiks_Cube_White.left(180-a3)
        Rubiks_Cube_White.fd(s4/3)
        Rubiks_Cube_White.left(180-a2)
        Rubiks_Cube_White.fd(s1)

    if Color == "Red":

        Rubiks_Cube_Red.fillcolor("red")
        Rubiks_Cube_Red.begin_fill()

        Rubiks_Cube_Red.setheading(90)

        Rubiks_Cube_Red.fd(s1)
        Rubiks_Cube_Red.right(a1)

        Rubiks_Cube_Red.fd(s2)
        Rubiks_Cube_Red.right(a2)

        Rubiks_Cube_Red.fd(s3)
        Rubiks_Cube_Red.right(a3)

        Rubiks_Cube_Red.fd(s4)
        Rubiks_Cube_Red.right(a4)

        Rubiks_Cube_Red.end_fill()

        Rubiks_Cube_Red.fd(s1/3)
        Rubiks_Cube_Red.right(a1)
        Rubiks_Cube_Red.fd(s2)
        Rubiks_Cube_Red.left(a3)
        Rubiks_Cube_Red.fd(s3/3)
        Rubiks_Cube_Red.left(a2)
        Rubiks_Cube_Red.fd(s2)

        Rubiks_Cube_Red.right(a4)
        Rubiks_Cube_Red.fd(s1/3)
        Rubiks_Cube_Red.right(a1)
        Rubiks_Cube_Red.fd(s2/3)
        Rubiks_Cube_Red.right(a2)
        Rubiks_Cube_Red.fd(s1)
        Rubiks_Cube_Red.left(180-a3)
        Rubiks_Cube_Red.fd(s4/3)
        Rubiks_Cube_Red.left(180-a2)
        Rubiks_Cube_Red.fd(s1)

Cube("Green", 200, 90, 200, 90, 200, 90, 200, 90)
Cube("White", 100, 45, 200, 135, 100, 45, 200, 135)
Cube("Red", 200, 45, 100, 135, 200, 45, 100, 135)

done()