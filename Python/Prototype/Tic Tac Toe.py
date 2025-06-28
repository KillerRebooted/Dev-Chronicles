from tkinter import *
import random

win = Tk()
win.title("Tic Tac Toe")
win.geometry("300x300")

def click(box, r, c, turn):
    
    players = {"Player 1": "X", "Player 2": "O"}

    if box.cget("text") == " ":
        box.configure(text=players[turn])

def main():
    for widget in win.winfo_children():
        widget.destroy()

    # Main Game
    r, c = 0, 0
    for _ in range(9):
        grid_box = Button(win, text=" ", font=("Helvetica", 22, "bold"))
        grid_box.grid(row=r, column=c, sticky="nsew")
        grid_box.configure(command=lambda grid_box=grid_box, r=r, c=c: click(grid_box, r, c, "Player 1"))

        win.rowconfigure(r, weight=1)
        win.columnconfigure(r, weight=1)

        c += 1

        if c > 2:
            c = 0
            r += 1

# Settings
def update_checkbox():
    if pvc_var == 1:
        computer_first_var.configure(state="normal")

pvc_var = IntVar()
computer_first_var = IntVar()
pvp_var = IntVar()

pvc_checkbox = Checkbutton(win, text="Player vs Computer", font=("Helvetica", 18, "bold"), variable=pvc_var, command=update_checkbox)
computer_first_checkbox = Checkbutton(win, text="Computer Plays First", font=("Helvetica", 12, "bold"), variable=computer_first_var, command=update_checkbox)

pvp_checkbox = Checkbutton(win, text="Player vs Player", font=("Helvetica", 18, "bold"), variable=pvp_var, command=update_checkbox)

pvc_checkbox.pack(padx=20)
computer_first_checkbox.pack(padx=(50, 0))
pvp_checkbox.pack(padx=(20, 64), pady=20)

start_button = Button(win, text="Start", font=("Helvetica", 15, "bold"), command=main)
start_button.pack()

win.mainloop()
