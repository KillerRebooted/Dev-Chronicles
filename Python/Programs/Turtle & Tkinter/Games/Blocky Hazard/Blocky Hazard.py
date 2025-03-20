from turtle import *
from functools import partial 
import winsound
from os import path

def main():

	global Ball_Shot, score, theme_no, font_size

	win = Screen()
	win.title("Blocky Hazard")
	win.bgcolor("white")
	win.setup(800, 600, 400, 100)
	win.tracer(0)
	
	Bar = Turtle()
	Bar.shape("square")
	Bar.shapesize(0.5, 5)
	Bar.penup()
	Bar.goto(0, -250)
	
	Ball = Turtle()
	Ball.shape("circle")
	Ball.shapesize(0.5, 0.5)
	Ball.penup()
	Ball.goto(Bar.xcor(), Bar.ycor()+14)

	Brick = Turtle()
	Brick.shape("square")
	Brick.shapesize(1, 3)
	Brick.penup()
	Brick.goto(-365, 285)
	Brick.hideturtle()

	Score = Turtle()
	Score.penup()
	Score.hideturtle()
	Score.goto(350, -200)

	score = 0
	theme_no = 0
	font_size = 16

	Bricks = []
	Removed_Bricks = []

	for i in range(-362, 365, 65):

		for j in range(285, 155, -25):

			Bricks.append([i, j])

			Brick.goto(i, j)
			Brick.stamp()

	win.update()
	
	Ball_Shot = False

	bounce_sdfx = lambda: winsound.PlaySound(f"{__file__.removesuffix(path.basename(__file__))}bounce.wav", winsound.SND_ASYNC)

	def themes(key):

		global theme_no

		#Background, Bar/Ball, Bricks

		theme = [["blue", "white", "red"], ["white", "black", "black"], ["white", "green", "red"], ["black", "#ffd700", "#ffd700"]]

		if key in ["Down", "s"]:

			if theme_no == 0:

				theme_no = len(theme)-1

			else:

				theme_no -= 1

		elif key in ["Up", "w"]:

			if theme_no == len(theme)-1:

				theme_no = 0

			else:

				theme_no += 1

		Brick.clear()

		for i in Bricks:

			Brick.color(theme[theme_no][2])

			Brick.goto(i)
			Brick.stamp()

		for i in Removed_Bricks:

			Brick.color(theme[theme_no][0])

			Brick.goto(i)
			Brick.stamp()

		win.bgcolor(theme[theme_no][0])
		Brick.color(theme[theme_no][0])
		Bar.color(theme[theme_no][1])
		Ball.color(theme[theme_no][1])
		Score.color(theme[theme_no][1])

		score_update()
		win.update()

	def score_update():

		global score, font_size

		Score.clear()

		if score < 0:

			score = 0

		Score.write(score, move=False, align="center", font=("Courier", int(font_size), "bold"))

		win.update()
	
	def move_left():

		global Ball_Shot
	
		if Bar.xcor() != -350:
	
			Bar.fd(-10)
	
		if not Ball_Shot:
			
			Ball.goto(Bar.xcor(), Bar.ycor()+14)
	
		win.update()
	
	def move_right():

		global Ball_Shot
	
		if Bar.xcor() != 340:
			
			Bar.fd(10)
	
		if not Ball_Shot:
			
			Ball.goto(Bar.xcor(), Bar.ycor()+14)
	
		win.update()

	def bar_move(mouse_coords):

		if Score.xcor() > 0:

			Bar.setx(-400 + mouse_coords.x)

		if not Ball_Shot:
			
			Ball.goto(Bar.xcor(), Bar.ycor()+14)
	
		win.update()
	
	def shoot():
	
		global Ball_Shot, score, font_size

		if not Ball_Shot:
			
			Ball_Shot = True
			space_deactivate()

			Ball.dx = 0.1
			Ball.dy = 0.1
		
		while True:
	
			win.update()
			
			Ball.setx(Ball.xcor() + Ball.dx)
			Ball.sety(Ball.ycor() + Ball.dy)
	
			if (Ball.xcor() > 385) or (Ball.xcor() < -390):
	
				Ball.dx *= -1
				bounce_sdfx()
	
			if Ball.ycor() > 290:
	
				Ball.dy *= -1
				bounce_sdfx()
	
			if (Ball.xcor() >= Bar.xcor()-60 and Ball.xcor() <= Bar.xcor()+60) and (Ball.ycor() >= -248 and Ball.ycor() <= -246):
	
				Ball.dy *= -1
				bounce_sdfx()

			if len(Bricks) == 0:

				turn = Score.towards(0, 0)

				Score.setheading(turn)

				Score.dx = -0.4
				Score.dy = 0.1

				while Score.xcor() >= 0:

					Score.clear()

					Score.setx(Score.xcor() + Score.dx)
					Score.sety(Score.ycor() + Score.dy)

					font_size += Score.dy

					Score.write(score, move=False, align="center", font=("Courier", int(font_size), "bold"))

				keys_deactivate()
				space_deactivate()

				done()

			for i in Bricks:

				if (Ball.xcor() >= i[0]-30 and Ball.xcor() <= i[0]+30) and (Ball.ycor() >= i[1]-10 and Ball.ycor() <= i[1]+10):

					Ball.dy *= -1
					bounce_sdfx()
					
					Brick.goto(i)
					Brick.stamp()
					
					Brick.goto(0, 0)
					Bricks.remove(i)
					Removed_Bricks.append(i)

					score += 1
					score_update()

			if Ball.ycor() < -285:

				Ball_Shot = False
				space_activate()
				Ball.goto(Bar.xcor(), Bar.ycor()+14)

				score -= 5
				score_update()
				
				win.update()
				break

	score_update()
	themes("Up")

	def space_activate():

		win.onkeyrelease(shoot, "space")

	def space_deactivate():

		win.onkeyrelease(None, "space")

	def keys_activate():

		win.onkeypress(move_left, "Left")
		win.onkeypress(move_right, "Right")
		win.onkeypress(move_left, "a")
		win.onkeypress(move_right, "d")
	
		win.onkeypress(partial(themes, "Up"), "Up")
		win.onkeypress(partial(themes, "Down"), "Down")
		win.onkeypress(partial(themes, "w"), "w")
		win.onkeypress(partial(themes, "s"), "s")

		canvas = win.getcanvas()
		canvas.bind("<Motion>", bar_move)

	def keys_deactivate():

		win.onkeypress(None, "Left")
		win.onkeypress(None, "Right")
		win.onkeypress(None, "a")
		win.onkeypress(None, "d")
	
		win.onkeypress(partial(themes, "Up"), "Up")
		win.onkeypress(partial(themes, "Down"), "Down")
		win.onkeypress(partial(themes, "w"), "w")
		win.onkeypress(partial(themes, "s"), "s")
	
	win.onkeypress(win.bye, "Escape")

	win.listen()
	
	keys_activate()
	space_activate()

	done()

if __name__ == "__main__":

	main()