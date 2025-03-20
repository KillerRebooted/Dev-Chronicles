from time import sleep
import customtkinter as ctk
import random as rand
import os
from playsound import playsound
import threading
from Backbone_of_Minesweeper import generate_board, make_move

#Working Directory
cur_dir = os.path.dirname(os.path.abspath(__file__))

#Tkinter Initiation
win = ctk.CTk(fg_color="#121212")
win.title("Minesweeper")
win.geometry("0x0")

w = win.winfo_screenwidth()
h = win.winfo_screenheight()

#Create Widgets
def create_board(size):
    global buttons, box_height, box_width

    box_width = w//size[0]
    box_height = h//size[1]

    buttons = []

    for r in range(size[1]):
        for c in range(size[0]):
            butt = ctk.CTkButton(win, text="", width=box_width, height=box_height, text_color="#000000", font=("Helvetica", 18, "bold"), fg_color="#FFFFFF", corner_radius=0, border_width=1, border_color="black", hover_color="#6bedbf", command=lambda r=r, c=c: click((r, c)))
            
            butt.grid(row=r, column=c)

            buttons.append(butt)

    win.update()

#Designer Functions
def center(win, screen_resolution, animation_time):

    x1, y1 = 0, 0

    while x1 != screen_resolution[0] or y1 != screen_resolution[1]:

        if x1 != screen_resolution[0]: x1 += screen_resolution[0]/(animation_time*10)
        if y1 != screen_resolution[1]: y1 += screen_resolution[1]/(animation_time*10)

        win.geometry(f"{int(x1)}x{int(y1)}")

        x2 = w//2 - win.winfo_width()//2
        y2 = h//2 - win.winfo_height()//2

        win.geometry(f"+{x2}+{y2}")

        sleep(0.008)
        win.update()

#Game Functions
def click(coords):
    global lost

    if not lost:

        size = board.shape[::-1]

        reveal = make_move(board, coords)

        if reveal == "Game Over!":
            lost = True
            return reveal_board(coords)

        idx = 0

        for r in range(size[1]):
            for c in range(size[0]):
                
                if (r, c) in reveal:
                    if board[r, c] == 0:
                        buttons[idx].configure(fg_color="#848a94")
                    else:
                        buttons[idx].configure(text=board[r, c])
                
                idx += 1

#Reveal Solution
def bomb_sound():

    playsound(f'{cur_dir}\\Files\\Explosion.mp3')

def reveal_board(coords):

    first_reveal=True

    idx = 0

    for mine in range(len(mine_placements)):

        if first_reveal:
            r, c = coords
            first_reveal = False
        else:
            r, c = rand.choice(mine_placements)

        mine_placements.remove((r, c))

        idx = 0

        for row in range(size[1]):
            for column in range(size[0]):
                if (r == row) and (c == column):
                    buttons[idx].configure(text="💣")
                    threading.Thread(target=bomb_sound, daemon=True).start()
                    win.after(int(rand.random()*1000))
                    win.update()
                idx += 1

    game_over = ctk.CTkLabel(win, text="Game Over!", font=("Helvetica", 36, "bold"), width=box_width*(0.8*size[0]))
    game_over.place(relx=0.1, rely=0.4, relheight=0.2)

    win.update()

#Main
def main(size, difficulty):
    global board, mine_placements, lost
        
    center(win, (w, h), 1)
    win.attributes('-fullscreen', True)

    lost = False

    create_board(size)

    board, mine_placements = generate_board(size, difficulty)

    win.mainloop()

if __name__ == "__main__":

    size = (20, 10)
    difficulty = 10

    main(size, difficulty)