from time import sleep
import customtkinter as ctk
from pynput import keyboard
from Sudoku_From_Image import scan_img

#Tkinter Initiation

win = ctk.CTk(fg_color="#0f172a")
win.title("Sudoku")
win.geometry("455x505")

text_color = "#f8fafc"
fg_color = "#1e293b"
corner_radius=4
border_width=1
border_color="#334155"
hover_color="#334155"

w = win.winfo_screenwidth()
h = win.winfo_screenheight()

#Create Widgets
def create_widgets():
    global buttons

    buttons = []

    for r in range(9):
        for c in range(9):
            butt = ctk.CTkButton(win, text="", width=50, height=50, text_color=text_color, font=("Helvetica", 18, "bold"), fg_color=fg_color, corner_radius=corner_radius, border_width=border_width, border_color=border_color, hover_color=hover_color)
            
            if c%3 == 2:
                butt.grid(row=r, column=c, padx=(0, 2))
            else:
                butt.grid(row=r, column=c, padx=(0, 0))

            if r%3 == 2:
                butt.grid(row=r, column=c, pady=(0, 2))
            else:
                butt.grid(row=r, column=c, pady=(0, 0))

            butt.bind("<Enter>", lambda event, butt=butt, r=r, c=c: update_value(butt, r, c))

            buttons.append(butt)

    def toggle_checkbox(btn, fast_solve):
        fast_solve.set(not fast_solve.get())

        if fast_solve.get():
            # Checked state (shows check symbol and active styling)
            btn.configure(
                text="☑ Fast Solve"
            )
        else:
            # Unchecked state (shows empty box symbol and normal button styling)
            btn.configure(
                text="☐ Fast Solve"
            )

    total_width = 454

    fast_solve = ctk.IntVar(value=0)
    checkbox = ctk.CTkButton(win, text="☐ Fast Solve", width=total_width/3, height=50, text_color=text_color, font=("Helvetica", 16, "bold"), fg_color=fg_color, corner_radius=corner_radius, border_width=border_width, border_color=border_color, hover_color=hover_color, command=lambda: toggle_checkbox(checkbox, fast_solve))
    checkbox.place(x=0, y=454)

    solve_on_screen = ctk.CTkButton(win, text="Solve on Screen", width=total_width/3, height=50, text_color=text_color, font=("Helvetica", 16, "bold"), fg_color=fg_color, corner_radius=corner_radius, border_width=border_width, border_color=border_color, hover_color=hover_color, state="disabled", command=lambda: scan_img(sudoku))
    solve_on_screen.place(x=total_width*2/3, y=454)

    solve_button = ctk.CTkButton(win, text="Solve!", width=total_width/3, height=50, text_color=text_color, font=("Helvetica", 16, "bold"), fg_color=fg_color, corner_radius=corner_radius, border_width=border_width, border_color=border_color, hover_color=hover_color, command=lambda: solve(sudoku, fast_solve.get(), fast_solve_checkbox=checkbox, solve_button=solve_button, solve_on_screen=solve_on_screen))
    solve_button.place(x=total_width/3, y=454)

    win.update()

#Initial Helpers
def convert(inp):

    converted = ""

    for i in range(0, len(inp), 3):
        for j in range(3):
            for k in range(3):
                for val in inp[i+k][j]:
                    converted += str(val) if val != " " else "."

    return converted

def reverse_convert(inp):

    converted = ""
    
    for r in range(9):
        for c in range(9):
            val = inp[r][c]
            converted += str(val) if val != -1 else " "

    return list(converted)

#Initial Sudoku Simplification
def make_simple_sudoku(inp):

    grid = {i:{j:[0, 0, 0] for j in range(3)} for i in range(9)}

    for idx, i in enumerate(inp):
        if i.isdigit():
            inp[idx] = int(i)
    
    iter = 0

    for i in range(0, len(grid), 3):
        for j in range(3):
            for k in range(3):
                grid[i+k][j] = [inp[iter], inp[iter + 1], inp[iter + 2]]
                iter += 3

    return grid

def initial_solve(puzzle):

    horizontal_listing = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    vertical_listing = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]

    def check_surroundings(coords):

        found_numbers = set()

        #Adding Numbers of Same Box to Set

        for line in puzzle[coords[0]].values():
            for num in range(3):
                found_numbers.add(line[num])

        #Finding the Boxes in Horizontal and Vertical Line

        for boxes in horizontal_listing:
            if coords[0] in boxes:
                horizontal_boxes = boxes

        for boxes in vertical_listing:
            if coords[0] in boxes:
                vertical_boxes = boxes

        #Checking Horizontal and Vertical Lines

        for box in horizontal_boxes:
            for column_value in puzzle[box][coords[1]]:
                found_numbers.add(column_value)

        for box in vertical_boxes:
            for row_value in [row[coords[2]] for row in puzzle[box].values()]:
                found_numbers.add(column_num)

        #print(f"{coords=}, {puzzle[coords[0]].values()=}, {found_numbers=}, {horizontal_boxes=}, {vertical_boxes=}")

        found_numbers.remove(" ")

        return found_numbers

    new_changes = True

    while new_changes:

        new_changes = False
        
        #Checking Boxes

        for box_num in (range(len(puzzle))):
            for line_num in range(3):
                for column_num in range(3):

                    digit = puzzle[box_num][line_num][column_num]

                    if digit == " ":
                        coords = [box_num, line_num, column_num]
                        vicinity = check_surroundings(coords)

                        possible_digit = 45 - sum(vicinity)

                        if possible_digit <= 9 and len(vicinity) == 8:
                            puzzle[box_num][line_num][column_num] = possible_digit
                            new_changes = True

    puzzle = convert(puzzle)

    return puzzle

#Helper Functions

def get_next_empty(puzzle):

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None

def is_valid(puzzle, r, c, guess):

    #Check if Guess is in the given Row
    if guess in puzzle[r]:
        return False

    #If Guess not in Row, check the Column for the Guess
    for row in puzzle:
        if row[c] == guess:
            return False
        
    row_start = r//3 * 3
    column_start = c//3 * 3
    for row in range(row_start, row_start+3):
        for column in range(column_start, column_start+3):
            if puzzle[row][column] == guess:
                return False
            
    return True

#Backtracking Solving Algorithm
def solve(puzzle, fast_solve, first_iter=True, fast_solve_checkbox=None, solve_button=None, solve_on_screen=None):
    global sudoku

    if first_iter:
        fast_solve_checkbox.configure(state="disabled")
        solve_button.configure(state="disabled")
        listener.stop()
        puzzle = convert_input(initial_solve(make_simple_sudoku(reverse_convert(sudoku))))

    row, column = get_next_empty(puzzle)

    if row is None:
        sudoku = puzzle
        return True

    for guess in range(1, 10):
        
        if is_valid(puzzle, row, column, guess):
            puzzle[row][column] = guess

            if not fast_solve:
                make_sudoku(puzzle)

            if solve(puzzle, fast_solve, first_iter=False, solve_on_screen=solve_on_screen):
                make_sudoku(puzzle)
                solve_on_screen.configure(state="normal")
                return True
            
        puzzle[row][column] = -1

    return False

#Puzzle Input
def convert_input(inp):

    temp_sudoku = [list(inp[i:i+9]) for i in range(0, len(inp), 9)]

    for r_idx, row in enumerate(temp_sudoku):
        for v_idx, val in enumerate(row):
            if val == ".":
                temp_sudoku[r_idx][v_idx] = -1
            temp_sudoku[r_idx][v_idx] = int(temp_sudoku[r_idx][v_idx])

    return temp_sudoku

#Tkinter Functions
def make_sudoku(grid):

    grid = [[val if val != -1 else " " for val in row] for row in grid]

    iter = 0

    for r in range(9):
        for c in range(9):
            buttons[iter].configure(text=grid[r][c])
            iter += 1

    win.update()

def update_value(button, r, c):
    global currently_clicked_button

    currently_clicked_button = (button, r, c)

def on_press(key, grid):
    global sudoku

    try:
        if key == keyboard.Key.backspace:
            currently_clicked_button[0].configure(text="")
            grid[currently_clicked_button[1]][currently_clicked_button[2]] = -1
        elif key.char.isdigit():
            currently_clicked_button[0].configure(text=key.char)
            grid[currently_clicked_button[1]][currently_clicked_button[2]] = int(key.char)

    except Exception as e:
        pass

def main():
    global listener

    create_widgets()

    make_sudoku(sudoku)

    listener = keyboard.Listener(on_press=lambda key: on_press(key, sudoku))
    listener.start()  # start to listen on a separate thread

    win.mainloop()

if __name__ == "__main__":

    sudoku = convert_input(scan_img())
    main()