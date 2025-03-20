import tkinter as tk
from tkinter.ttk import Progressbar
import time, random

win1 = tk.Tk()
win1.title("Mind Reader")
win1.configure(background = "#121212")
win1.bind("<Escape>", lambda event: win1.destroy())
win1.geometry("400x250+760+415")

def read_my_mind():

    win2 = tk.Tk()
    win2.title("Reading Mind...")
    win2.configure(background = "#121212")
    win2.bind("<Escape>", lambda event: win2.destroy())
    win2.geometry("400x175+760+415")

    thoughts = ["Analyzing Brainwaves...", "Consulting Fortune Tellers...", "Looking for the Guy Who Asked...", "Attending Probablity Classes...", "Looking for Ankur Sir...", "Doing Your Mom...", "Mewing...", "Applying Complex Algorithms...", "Looking for a Handsome User...", "Seeking Salvation..."]

    thinker = tk.Label(win2, font="Helvetica 8 bold", text="Analyzing Brainwaves...", background="#121212", fg="white")
    thinker.place(x=100, y=20, height=50, width=200)
    
    progress_bar = Progressbar(win2, length=350, mode='determinate')
    progress_bar.place(x=25, y=100)

    for i in range(0, 1001):
        progress_bar["value"] = i/10
        time.sleep(0.01)

        if progress_bar["value"]%15 == 0:
            try:
                thinker.configure(text=thoughts.pop(random.randint(0, len(thoughts)-1)))
            except:
                thinker.configure(text=thoughts[0])

        win1.update()

    thinker.configure(text=f"You were thinking of {entry.get()}", font="Helvetica 12 bold")

    progress_bar.destroy()

label = tk.Label(win1, text="Think of a Number between 1 and 10", font="Helvetica 15 bold", background="#121212", fg="white")
label.place(x=25, y=20, height=20, width=350)

entry = tk.Entry(win1, font="Helvetica 15 bold")
entry.place(x=100, y=60, height=40, width=200)

button = tk.Button(win1, text="Read My Mind", font="Helvetica 10 bold", background="#121212", fg="white", command=read_my_mind)
button.place(x=150, y=150, height=40, width=100)

win1.mainloop()