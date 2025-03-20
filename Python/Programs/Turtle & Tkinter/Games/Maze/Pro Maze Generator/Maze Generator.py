from turtle import Turtle, Screen, done
import random

def main(maze_size, spiral_tendency, total_maze_size):

	global z, run, dist, find_solution

	if total_maze_size % maze_size != 0:

		quit()

	win = Screen()
	win.title("Maze Generator")
	win.bgcolor("black")
	win.setup(800, 600, 400, 100)
	win.screensize(total_maze_size + 100, total_maze_size + 100)
	win.tracer(0)

	Boundary = Turtle()
	Boundary.pensize(maze_size - 5)
	Boundary.hideturtle()
	Boundary.penup()
	Boundary.goto(-(0.5 * total_maze_size), -(0.5 * total_maze_size))
	Boundary.seth(90)
	Boundary.pencolor("white")
	Boundary.pendown()

	Maze = Turtle()
	Maze.shape("square")
	Maze.shapesize(0.03 * maze_size)
	Maze.hideturtle()
	Maze.fillcolor("white")
	Maze.pencolor("white")
	Maze.penup()

	End = Turtle()
	End.shape("square")
	End.shapesize(0.04 * maze_size)
	End.penup()
	End.hideturtle()

	Solution = Turtle()
	Solution.pensize(0.3 * maze_size)
	Solution.pencolor("green")
	Solution.hideturtle()
	Solution.penup()

	for i in range(4):

		Boundary.fd(total_maze_size)
		Boundary.right(90)

	win.update()

	Maze.goto(random.choice([-(0.5 * total_maze_size), (0.5 * total_maze_size)]), random.choice([(0.5 * total_maze_size), -(0.5 * total_maze_size)]))

	start_loc = random.choice("xy")

	Range = range(int(-(0.5 * total_maze_size)+maze_size), int((0.5 * total_maze_size)+1-maze_size), maze_size)

	if start_loc == "x":

		Maze.setx(random.choice(Range))

	else:

		Maze.sety(random.choice(Range))

	if Maze.xcor() == -(0.5 * total_maze_size):

		Maze.seth(0)
		
	elif Maze.xcor() == (0.5 * total_maze_size):

		Maze.seth(180)
		
	elif Maze.ycor() == (0.5 * total_maze_size):

		Maze.seth(270)
	
	else:

		Maze.seth(90)

	start_loc = [Maze.xcor(), Maze.ycor()]

	Maze_Locations = []
	find_solution = []

	for i in range(int(-(0.5 * total_maze_size)), int((0.5 * total_maze_size)+1), maze_size):

		Maze_Locations.append([i, (0.5 * total_maze_size)])
		Maze_Locations.append([i, -(0.5 * total_maze_size)])

	for i in range(int(-(0.5 * total_maze_size)), int((0.5 * total_maze_size)+1), maze_size):

		Maze_Locations.append([-(0.5 * total_maze_size), i])
		Maze_Locations.append([(0.5 * total_maze_size), i])

	Maze_Locations.append(start_loc)
	find_solution.append(start_loc)

	z = -1

	def check_possible_directions():

		global possible_directions, z, run, dist, find_solution, solution_visible

		possible_directions = []

		Maze.penup()

		for i in [90, 0, -90, 180]:

			Maze.left(i)
			
			if Maze.heading() in [0, 360]:
				Maze.setx(Maze.xcor()+maze_size)

				delta = +maze_size

			elif Maze.heading() in [180, -180]:
				Maze.setx(Maze.xcor()-maze_size)

				delta = -maze_size

			elif Maze.heading() in [90, -270]:
				Maze.sety(Maze.ycor()+maze_size)

				delta = +maze_size

			elif Maze.heading() in [270, -90]:
				Maze.sety(Maze.ycor()-maze_size)

				delta = -maze_size

			if [Maze.xcor(), Maze.ycor()] not in Maze_Locations:

				if i == 0:

					possible_directions.extend([Maze.heading()] * spiral_tendency)

				else:

					possible_directions.append(Maze.heading())

			if Maze.heading() in [0, 360]:
				Maze.setx(Maze.xcor()-delta)

			elif Maze.heading() in [180, -180]:
				Maze.setx(Maze.xcor()-delta)

			elif Maze.heading() in [90, -270]:
				Maze.sety(Maze.ycor()-delta)

			elif Maze.heading() in [270, -90]:
				Maze.sety(Maze.ycor()-delta)

			Maze.right(i)

		if len(possible_directions) == 0:

			run = True

			if Maze_Locations[z] == start_loc:

				Maze.goto(furthest_x_y)
				Maze.fillcolor("red")
				Maze.showturtle()
				Maze.penup()

				End.goto(start_loc)
				End.fillcolor("blue")
				End.showturtle()

				solution = find_solution[find_solution.index(start_loc) : find_solution.index(furthest_x_y)]

				final_solution = []

				for i in solution:

					if not solution.count(i) > 1:

						final_solution.append(i)

				def up():

					Maze.sety(Maze.ycor()+maze_size)

					win.update()

				def down():

					Maze.sety(Maze.ycor()-maze_size)

					win.update()

				def left():

					Maze.setx(Maze.xcor()-maze_size)

					win.update()

				def right():

					Maze.setx(Maze.xcor()+maze_size)

					win.update()

				def show_solution():

					global solution_visible

					if not solution_visible:

						Solution.penup()
	
						Solution.goto(final_solution[0])
	
						for i in final_solution[1:]:
	
							Solution.pendown()
	
							Solution.goto(i)
	
						Solution.goto(furthest_x_y)

						solution_visible = True

					else:

						Solution.clear()

						solution_visible = False

					win.update()

				solution_visible = False

				win.onkeypress(up, "w")
				win.onkeypress(down, "s")
				win.onkeypress(left, "a")
				win.onkeypress(right, "d")

				win.onkeypress(show_solution, "`")
				
				win.update()
				done()

			Maze.goto(Maze_Locations[z])
			find_solution.append(Maze_Locations[z])

			dist -= 1
			z -= 1

		else:

			run = False

			if find_solution.count(find_solution[-1]) > 1:

				find_solution.pop(-1)

	dist = 0
	furthest_distance = 0
		
	while True:

		for i in range(2):	

			if Maze.heading() in [0, 360]:
				
				Maze.setx(Maze.xcor()+maze_size/2)
	
			elif Maze.heading() in [180, -180]:
				
				Maze.setx(Maze.xcor()-maze_size/2)
	
			elif Maze.heading() in [90, -270]:
				
				Maze.sety(Maze.ycor()+maze_size/2)
	
			elif Maze.heading() in [270, -90]:
				
				Maze.sety(Maze.ycor()-maze_size/2)
	
			Maze.stamp()

		dist += 1

		if dist > furthest_distance:

			furthest_distance = dist

			furthest_x_y = [Maze.xcor(), Maze.ycor()]

		Maze_Locations.append([Maze.xcor(), Maze.ycor()])
		find_solution.append([Maze.xcor(), Maze.ycor()])

		run = True
					
		while run:

			check_possible_directions()

		Maze.seth(random.choice(possible_directions))
		z = -1

		win.update()

		win.onkeypress(win.bye, "Escape")

		win.listen()

if __name__ == "__main__":

	main(20, 2, 700)

	#Maze Size: Smaller Number - Bigger Maze (Should be Divisible by Total Maze Size) (NOTE: Anything Smaller than 10 is not Recommended)

	#Spiral Tendency: Bigger Number - More Spiral (0 or 1 for Least Spiral (Not Recommended), 2 for Avg. Spiral (Recommended), 3-any number for Highly Spiral Maze (If you prefer it IG))

	#Total Maze Size: Eg: 500 means a 500x500 Maze (NOTE: Anything Smaller than 300 is not Recommended)
