import random
import colorsys
import time
from turtle import *

def get_luminance(r, g, b):
    """Calculates perceived brightness on a 0-255 scale."""
    return 0.299 * r + 0.587 * g + 0.114 * b

def get_random_contrast_color(bg_rgb):
    """Generates a random color with guaranteed contrast against the background."""
    bg_brightness = get_luminance(*bg_rgb)

    # 1. Any random hue on the color wheel (0.0 to 1.0)
    hue = random.random()

    # 2. Keep saturation high for rich, distinct colors (70% - 100%)
    saturation = random.uniform(0.7, 1.0)

    # 3. Choose lightness based on background brightness
    if bg_brightness > 128:
        # Background is light -> pick a deep, dark color
        lightness = random.uniform(0.15, 0.35)
    else:
        # Background is dark -> pick a bright, pastel/neon color
        lightness = random.uniform(0.70, 0.90)

    # Convert HLS float values back to 0-255 RGB integers
    r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
    return (int(r * 255), int(g * 255), int(b * 255))

def draw_pole(pole: Turtle, x: int, y: int, height: int, width: int):
    pole.goto(x, y)
    pole.seth(0)
    pole.begin_fill()
    pole.pd()
    pole.fd(width/2)
    pole.left(90)
    pole.fd(height)
    pole.left(90)
    pole.fd(width)
    pole.left(90)
    pole.fd(height)
    pole.left(90)
    pole.fd(width/2)
    pole.end_fill()
    pole.pu()

def update_disks(n: int, disk_turtles: list, disk_height: int, disk_gap: int, pole_a: tuple, pole_b: tuple, pole_c: tuple):

    x, y = pole_a
    for disk in range(1, n+1):
        disk_x = x
        disk_y = y + (disk - 1) * (disk_height + disk_gap) + disk_height / 2

        disk_turtles[n - disk].goto(disk_x, disk_y)
        disk_turtles[n - disk].st()
            
def move_disk(win: Screen, disk: Turtle, pole_max_heights: list, transit_height: int, delta_height: int, start: tuple, end: tuple, poles: list):
    disk.goto(disk.xcor(), transit_height)
    disk.goto(end[0], transit_height)
    disk.goto(end[0], end[1] + pole_max_heights[poles.index(end)])

    pole_max_heights[poles.index(start)] -= delta_height
    pole_max_heights[poles.index(end)] += delta_height

def An(num):
    return 2**num - 1

def toh(win: Screen, set_tracer_zero: bool, move_counter: Turtle, total_moves: int, moves_completed: list, disk_turtles: list, pole_max_heights: list, transit_height: int, delta_height: int, n: int, start: tuple, mid: tuple, end: tuple, poles: list):

    if n == 1:
        move_disk(win, disk_turtles[n-1], pole_max_heights, transit_height, delta_height, start, end, poles)
        moves_completed[0] += 1
        win.tracer(0)
        move_counter.clear()
        move_counter.write(f"Total Moves: {total_moves:,} | Moves Completed: {moves_completed[0]:,} | Moves Remaining: {total_moves - moves_completed[0]:,}", align="center", font=("Arial", 16, "normal"))
        win.update()
        if not set_tracer_zero: win.tracer(1)
    
    else:

        toh(win, set_tracer_zero, move_counter, total_moves, moves_completed, disk_turtles, pole_max_heights, transit_height, delta_height, n-1, start, end, mid, poles)

        move_disk(win, disk_turtles[n-1], pole_max_heights, transit_height, delta_height, start, end, poles)
        moves_completed[0] += 1
        win.tracer(0)
        move_counter.clear()
        move_counter.write(f"Total Moves: {total_moves:,} | Moves Completed: {moves_completed[0]:,} | Moves Remaining: {total_moves - moves_completed[0]:,}", align="center", font=("Arial", 16, "normal"))
        win.update()
        if not set_tracer_zero: win.tracer(1)

        toh(win, set_tracer_zero, move_counter, total_moves, moves_completed, disk_turtles, pole_max_heights, transit_height, delta_height, n-1, mid, start, end, poles)

def main(set_tracer_zero: bool, speed: int):

    n = int(input("Enter the number of Disks: "))

    win = Screen()
    win.title("Tower of Hanoi")
    win.colormode(255)
    win.bgcolor(bgcolor:= (20, 25, 40))
    win.tracer(0)

    pole = Turtle(visible=False)
    pole.speed(0)
    pole.pu()
    pole.pencolor(get_random_contrast_color(bgcolor))

    pole_start_x = 0
    pole_start_y = -200
    pole_gap = 300
    pole_a = (pole_start_x - pole_gap, pole_start_y)
    pole_b = (pole_start_x, pole_start_y)
    pole_c = (pole_start_x + pole_gap, pole_start_y)
    poles = [pole_a, pole_b, pole_c]
    pole_height = 400

    disk_width_unit = (pole_gap - 20) / n
    disk_gap = 4
    disk_height = (pole_height - (n-1)*disk_gap) / (n + 2)
    
    pole_width = disk_width_unit / 2

    draw_pole(pole, pole_a[0], pole_a[1], pole_height, pole_width)
    draw_pole(pole, pole_b[0], pole_b[1], pole_height, pole_width)
    draw_pole(pole, pole_c[0], pole_c[1], pole_height, pole_width)

    total_moves = An(n)
    moves_completed = [0]
    move_counter = Turtle(visible=False)
    move_counter.pencolor(get_random_contrast_color(bgcolor))
    move_counter.pu()
    move_counter.goto(0, pole_start_y + pole_height + 100)
    move_counter.write(f"Total Moves: {total_moves:,} | Moves Completed: {moves_completed[0]:,} | Moves Remaining: {total_moves - moves_completed[0]:,}", align="center", font=("Arial", 16, "normal"))

    delta_height = disk_height + disk_gap
    pole_max_heights = [delta_height*n + disk_height/2 , disk_height/2, disk_height/2]
    transit_height = pole_start_y + pole_height + disk_height

    disk_turtles = []
    for i in range(n):
        disk = Turtle("square", visible=False)
        color = get_random_contrast_color(bgcolor)
        disk.pencolor(color)
        disk.fillcolor(color)
        disk.speed(speed)
        disk.shapesize(stretch_wid=disk_height/20, stretch_len=disk_width_unit * (i + 1) / 20, outline=disk_gap/2)
        disk.pu()

        disk_turtles.append(disk)
    
    update_disks(n, disk_turtles, disk_height, disk_gap, pole_a, pole_b, pole_c)

    win.update()
    time.sleep(1)

    if not set_tracer_zero:
        win.tracer(1)

    toh(win, set_tracer_zero, move_counter, total_moves, moves_completed, disk_turtles, pole_max_heights, transit_height, delta_height, n, pole_a, pole_b, pole_c, poles)

    done()

if __name__ == "__main__":
    # set_tracer_zero: True for faster execution, False for slower execution
    # speed: Speed increases with number. 0 is highest. Affects speed if set_tracer_zero=False
    main(set_tracer_zero=False, speed=8)