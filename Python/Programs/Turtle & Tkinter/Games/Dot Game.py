from turtle import *

win = Screen()
win.title("Dot Game")
win.bgcolor("white")
win.setup(700, 650, 400, 100)
win.tracer(0)

dots = Turtle()
dots.width(2)
dots.penup()
dots.speed(0)
dots.hideturtle()

Player1 = Turtle("circle")
Player1.shapesize(0.5, 0.5)
Player1.pencolor("blue")
Player1.width(2)

P1 = Turtle()
P1.pencolor("blue")
P1.hideturtle()
P1.penup()

Player2 = Turtle("circle")
Player2.shapesize(0.5, 0.5)
Player2.pencolor("red")
Player2.width(2)

P2 = Turtle()
P2.pencolor("red")
P2.hideturtle()
P2.penup()

Chance = Turtle()
Chance.hideturtle()
Chance.penup()

Score = Turtle()
Score.hideturtle()
Score.penup()

Result = Turtle()
Result.hideturtle()
Result.penup()

Info = Turtle()
Info.hideturtle()
Info.penup()

Info.goto(0, -300)
Info.write("R - Reset Chance    Right Click - Mark Box", move=False, align="center", font=("Courier", 11, "bold"))

move = 0
num = 1

Score_P1 = 0
Score_P2 = 0

def retry():

    global move

    move = 0

def click(x, y):

    global num, move

    if (x > 235 or x < -235) or (y > 235 or x < -235) or ((25 * round(x/25))%50 == 0) or ((25 * round(y/25))%50 == 0):

        return

    else:

        if (num == 2) and (move == 0):

            Player2.penup()
            Player2.goto(25 * round(x/25), 25 * round(y/25))
            Player2.pendown()

            move = 1
            num = 2

        elif (num == 2) and (move == 1):

            if (Player2.xcor() == 25 * round(x/25)) or (Player2.ycor() == 25 * round(y/25)): 

                if (not abs(Player2.xcor() - 25 * round(x/25)) > 50) and (not abs(Player2.ycor() - 25 * round(y/25)) > 50):

                    Player2.goto(25 * round(x/25), 25 * round(y/25))

                    move = 0
                    num = 1

        elif (num == 1) and (move == 0):

            Player1.penup()
            Player1.goto(25 * round(x/25), 25 * round(y/25))
            Player1.pendown()

            move = 1
            num = 1

        else:

            if (Player1.xcor() == 25 * round(x/25)) or (Player1.ycor() == 25 * round(y/25)):

                if (not abs(Player1.xcor() - 25 * round(x/25)) > 50) and (not abs(Player1.ycor() - 25 * round(y/25)) > 50):

                    Player1.goto(25 * round(x/25), 25 * round(y/25))

                    move = 0
                    num = 2

        chance = f"Player {num}"

        Chance.clear()
        Chance.goto(0, 280)

        if num == 1:

            Chance.pencolor("blue")
            Chance.write(chance, move=False, align="center", font=("Courier", 20, "bold"))

        else:

            Chance.pencolor("red")
            Chance.write(chance, move=False, align="center", font=("Courier", 20, "bold"))

    win.update()

def score(x, y):

    global Score_P1, Score_P2, num, move

    if (x > 235 or x < -235) or (y > 235 or x < -235):

        return

    else:
    
        Score.goto(50 * round(x/50), 50 * round(y/50)-10)

        if num == 2:
            
            Score.pencolor("blue")
            Score.write("P1", move=False, align="center", font=("Courier", 11, "bold"))

            Score_P1 += 1

            num = 1
            move = 0

        else:
            
            Score.pencolor("red")
            Score.write("P2", move=False, align="center", font=("Courier", 11, "bold"))

            Score_P2 += 1

            num = 2
            move = 0

        P1.clear()
        P2.clear()

        P1.goto(-150, 280)
        P2.goto(150, 280)

        P1.write(Score_P1, move=False, align="center", font=("Courier", 14, "bold"))
        P2.write(Score_P2, move=False, align="center", font=("Courier", 14, "bold"))

        chance = f"Player {num}"

        Chance.clear()
        Chance.goto(0, 280)

        if num == 1:

            Chance.pencolor("blue")
            Chance.write(chance, move=False, align="center", font=("Courier", 20, "bold"))

        else:

            Chance.pencolor("red")
            Chance.write(chance, move=False, align="center", font=("Courier", 20, "bold"))

    win.update()

def result():

    if Score_P1 > Score_P2:

        Chance.clear()
        Result.goto(0, 280)
        Result.pencolor("blue")
        Result.write("Player 1 WINS!", move=False, align="center", font=("Courier", 20, "bold"))

        exitonclick()

    elif Score_P2 > Score_P1:

        Chance.clear()
        Result.goto(0, 280)
        Result.pencolor("red")
        Result.write("Player 2 WINS!", move=False, align="center", font=("Courier", 20, "bold"))

        exitonclick()

    else:

        Chance.clear()
        Result.goto(-16, 280)
        Result.pencolor("blue")
        Result.write("DR", move=False, align="center", font=("Courier", 20, "bold"))
        Result.goto(16, 280)
        Result.pencolor("red")
        Result.write("AW", move=False, align="center", font=("Courier", 20, "bold"))

    win.update()


j = 250

for i in range(-225, 226, 50):

    for j in range(225, -226, -50):    
        
        dots.goto(i, j)
        dots.dot(5)

chance = f"Player {num}"

Chance.clear()
Chance.goto(0, 280)

if num == 1:
        
    Chance.pencolor("blue")
    Chance.write(chance, move=False, align="center", font=("Courier", 20, "bold"))

else:

    Chance.pencolor("red")
    Chance.write(chance, move=False, align="center", font=("Courier", 20, "bold"))

P1.goto(-150, 280)
P2.goto(150, 280)
    
P1.write(Score_P1, move=False, align="center", font=("Courier", 14, "bold"))
P2.write(Score_P2, move=False, align="center", font=("Courier", 14, "bold"))

num = 1

onscreenclick(click, btn=1)
onscreenclick(score, btn=3)
win.onkeypress(result, "space")
win.onkeypress(retry, "r")
win.onkeypress(win.bye, "Escape")

win.listen()

mainloop()