from tkinter import *
import random

win = Tk()
win.title("Tic Tac Toe")
win.geometry("300x300")
win.resizable(False, False)

# Get Moves from the Board
def get_moves():
    global moves
    
    try:
        moves = ""
        for button in win.winfo_children():
            moves += button.cget("text")
        return moves
    except:
        return " " * 9

# Check if there is a Winner
def check_win(
        win_conditions = {
        "rows": ((0, 1, 2), (3, 4, 5), (6, 7, 8)),     # Rows
        "columns": ((0, 3, 6), (1, 4, 7), (2, 5, 8)),  # Columns
        "diagonals": ((0, 4, 8), (2, 4, 6))            # Diagonals
    }
    ):

    # Check for Win Conditions
    for category in win_conditions.keys():
        for condition in win_conditions[category]:
            if moves[condition[0]] == moves[condition[1]] == moves[condition[2]] != " ":
                # Display Winner
                winner = 1 if moves.count(" ")%2 == 0 else 2
                return winner
    
    return 0

# All Game Rules for Tic Tac Toe
def game_rule(box, r, c):
    global usable_boxes, game_over

    if not game_over:

        usable_boxes.remove((r, c))

        players = {1: "X", 2: "O"}

        # Get all Moves
        moves = get_moves()

        # Create Symbol based on which Player's turn it is
        if box.cget("text") == " ":

            if moves.count(" ")%2 != 0:
                turn = 1
            else:
                turn = 2

            box.configure(text=players[turn])

        # Get all Moves
        moves = get_moves()

        winner = check_win()

        if winner:
            print(f"Player {winner} wins!")
            game_over = True
            return

        # Bot Logic if Player vs Computer
        if pvc_var.get() == 1:
            computer_move = random.choice(usable_boxes)
            for widget in win.winfo_children():
                if widget.grid_info()["row"] == computer_move[0] and widget.grid_info()["column"] == computer_move[1]:
                    widget.configure(text=players[2])
                    usable_boxes.remove(computer_move)
                    break

def main():
    global usable_boxes, game_over

    if (pvc_var.get() == 0) and (pvp_var.get() == 0):
        return

    # Clear Setting Widgets
    for widget in win.winfo_children():
        widget.destroy()

    # Create Tic Tac Toe Grid
    r, c = 0, 0
    usable_boxes = []
    for _ in range(9):
        grid_box = Button(win, text=" ", font=("Helvetica", 22, "bold"))
        grid_box.grid(row=r, column=c, sticky="nsew")
        grid_box.configure(command=lambda grid_box=grid_box, r=r, c=c: game_rule(grid_box, r, c))

        win.rowconfigure(r, weight=1)
        win.columnconfigure(c, weight=1)

        usable_boxes.append((r, c))

        c += 1

        if c > 2:
            c = 0
            r += 1
    

    game_over = False

# -----> Settings

# Update which Checkbox is enabled based on the selected Game Mode
def update_checkbox(change):
    
    if change == "pvc":
        if pvc_var.get() == 1:
            computer_first_checkbox.configure(state="normal")
            pvp_var.set(0)
        else:
            computer_first_var.set(0)
            computer_first_checkbox.configure(state="disabled")
    elif change == "computer_first":
        computer_first_checkbox.configure(state="disabled")
    elif change == "pvp":
        computer_first_var.set(0)
        computer_first_checkbox.configure(state="disabled")
        pvc_var.set(0)

# Setting Page
pvc_var = IntVar()
computer_first_var = IntVar()
pvp_var = IntVar()

pvc_checkbox = Checkbutton(win, text="Player vs Computer", font=("Helvetica", 18, "bold"), variable=pvc_var, command=lambda: update_checkbox("pvc"))
computer_first_checkbox = Checkbutton(win, text="Computer Plays First", font=("Helvetica", 12, "bold"), variable=computer_first_var, command=lambda: update_checkbox(None))

pvp_checkbox = Checkbutton(win, text="Player vs Player", font=("Helvetica", 18, "bold"), variable=pvp_var, command=lambda: update_checkbox("pvp"))

pvc_checkbox.pack(padx=20)
computer_first_checkbox.pack(padx=(50, 0))
pvp_checkbox.pack(padx=(20, 64), pady=20)

start_button = Button(win, text="Start", font=("Helvetica", 15, "bold"), command=main)
start_button.pack()

# Disable computer_first_checkbox by default
update_checkbox("computer_first")

win.mainloop()