from turtle import *
import random
import colorsys

def get_spectrum_colors(n):
    colors = []
    for i in range(n):
        # Step through hue from 0.0 to 1.0 (excluding 1.0 to avoid repeating Red)
        hue = i / n
        
        # colorsys.hsv_to_rgb takes values in [0.0, 1.0]
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        
        # Convert to 0-255 integers or Hex codes
        rgb_255 = (int(r * 255), int(g * 255), int(b * 255))
        
        colors.append(rgb_255)
    
    return colors

def visualize_elements(turtle_elements, starting_x, starting_y, sizing_factor, updated_elements=None):
    if updated_elements == None:
        for i, turtle_element in enumerate(turtle_elements):
            stretch_wid, stretch_len, outline = turtle_element.shapesize()
            turtle_element.goto(starting_x + stretch_len/sizing_factor * ( 1/2 + i ), starting_y+stretch_wid/sizing_factor/2)

    else:
        for turtle_element in updated_elements:
            stretch_wid, stretch_len, outline = turtle_element.shapesize()
            i = turtle_elements.index(turtle_element)
            turtle_element.goto(starting_x + stretch_len/sizing_factor * ( 1/2 + i ), starting_y+stretch_wid/sizing_factor/2)

def algorithm(win, reduced_updates, algo_name, turtle_elements, starting_x, starting_y, sizing_factor):
    if algo_name == "bubble":
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(turtle_elements)-1):
                if turtle_elements[i].shapesize()[0] > turtle_elements[i+1].shapesize()[0]:
                    turtle_elements[i], turtle_elements[i+1] = turtle_elements[i+1], turtle_elements[i]
                    updated_elements = [turtle_elements[i], turtle_elements[i+1]]
                    swapped = True
                    visualize_elements(turtle_elements, starting_x, starting_y, sizing_factor, updated_elements)
                    if not reduced_updates: win.update()
            win.update()

    if algo_name == "selection":
        i = 0
        while i < len(turtle_elements):
            min_index = i
            for j in range(i+1, len(turtle_elements)):
                if turtle_elements[j].shapesize()[0] < turtle_elements[min_index].shapesize()[0]:
                    min_index = j
            if min_index != i:
                turtle_elements[i], turtle_elements[min_index] = turtle_elements[min_index], turtle_elements[i]
                updated_elements = [turtle_elements[i], turtle_elements[min_index]]
                visualize_elements(turtle_elements, starting_x, starting_y, sizing_factor, updated_elements)
                win.update()
            i += 1

    if algo_name == "double_selection":
        i = 0
        j = len(turtle_elements) - 1
        while i < j:
            min_index = i
            max_index = j
            for k in range(i, j+1):
                comparison = turtle_elements[k].shapesize()[0]
                if comparison < turtle_elements[min_index].shapesize()[0]:
                    min_index = k
                if comparison > turtle_elements[max_index].shapesize()[0]:
                    max_index = k
            if min_index != i:
                turtle_elements[i], turtle_elements[min_index] = turtle_elements[min_index], turtle_elements[i]
                updated_elements = [turtle_elements[i], turtle_elements[min_index]]
                visualize_elements(turtle_elements, starting_x, starting_y, sizing_factor, updated_elements)
                win.update()

            if max_index == i:
                max_index = min_index

            if max_index != j:
                turtle_elements[j], turtle_elements[max_index] = turtle_elements[max_index], turtle_elements[j]
                updated_elements = [turtle_elements[j], turtle_elements[max_index]]
                visualize_elements(turtle_elements, starting_x, starting_y, sizing_factor, updated_elements)
                win.update()
            i += 1
            j -= 1

def main(set_tracer_zero, reduced_updates, speed, algo_name):

    n = int(input("Enter the number of Elements: "))
    elements = list(range(1, n + 1))

    win = Screen()
    win.title("Sorting Visualizer")
    win.colormode(255)
    win.bgcolor(bgcolor:= (20, 25, 40))
    if set_tracer_zero: win.tracer(0)

    h_max = 400
    sorting_area_width = 800
    starting_x = -sorting_area_width / 2
    starting_y = -h_max / 2

    sizing_factor = 1/20
    element_width = sorting_area_width / n
    element_height_factor = h_max / max(elements)
    elements = [element*element_height_factor for element in elements]

    colors = get_spectrum_colors(n)
    turtle_elements = []
    win.tracer(0)
    for i in range(n):
        turtle_element = Turtle("square", visible=False)
        turtle_element.shapesize(stretch_wid=elements[i]*sizing_factor, stretch_len=element_width*sizing_factor)
        turtle_element.pencolor(colors[i])
        turtle_element.fillcolor(colors[i])
        turtle_element.pu()
        turtle_element.speed(speed=speed)
        turtle_elements.append(turtle_element)
    random.shuffle(turtle_elements)
    visualize_elements(turtle_elements, starting_x, starting_y, sizing_factor)
    [turtle_element.st() for turtle_element in turtle_elements]
    win.update()
    if not set_tracer_zero: win.tracer(1)

    algorithm(win, reduced_updates, algo_name, turtle_elements, starting_x, starting_y, sizing_factor)

    done()

if __name__ == "__main__":
    # set_tracer_zero: True for faster execution, False for slower execution
    # reduced_updates: True for faster execution, False for slower execution. Only works if set_tracer_zero=True
    # speed: Speed increases with number. 0 is highest. Affects speed if set_tracer_zero=False
    # algo_name: bubble, selection, double_selection
    main(set_tracer_zero=True, reduced_updates=True, speed=2, algo_name="double_selection")