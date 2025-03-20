import requests
from bs4 import BeautifulSoup
from threading import Thread
import pygame as pg
import time, os

hands = "both" #LH, RH, both. If "LH" or "RH" is chosen, the notes from that hand will not be played. "both" means, both hands will be played
pitch = 0 #Increase Pitch to change the notes to High or Deep Notes--> integer
extra = 0 #Extra Delay to Slow Down Music --> float (recommended)
song = "https://pianoletternotes.blogspot.com/2018/07/love-scenario-by-ikon.html"

#Extracting Notes

url = requests.get(song)
url.encoding = "utf-8"

soup = BeautifulSoup(url.text, 'html.parser')

code = soup.find_all("code")[0]

notes = code.get_text().strip().split("\n")
if hands != "both":
    notes = [i for i in notes if f"{hands}:" not in i]

group = []
grouped_notes = []

for i in notes:

    if i != "":
        group.append(i)
    else:
        grouped_notes.append(tuple(group))
        group = []

duration_prev = 0
def merge(notes, chord, extra):

    global duration_prev

    first = True

    clean_notes = tuple(i.lstrip("RH:").lstrip("LH:") for i in notes)

    letter_notes = []
    duration = []
    count = 0

    for i in range(26):

        check = letter_notes.copy()

        for j in clean_notes:
            if j[i+2].isalpha():
                letter_notes.append(f"{j[i+2]}{int(j[0]) + chord}")

                if first:
                    add = float(f"{count/10 : .1f}") + duration_prev
                    add += extra
                    duration.append(add)
                    first = False
                else:
                    add = float(f"{count/10 : .1f}")
                    add += extra
                    duration.append(add)

                count = 0

        if letter_notes == check:
            count += 1
    
    duration_prev = float(f"{count/10 : .1f}")

    return letter_notes, duration

letter_notes = []
duration = []

for i in grouped_notes:
    result = merge(i, pitch, extra)

    letter_notes.extend(result[0])
    duration.extend(result[1])

#Song Code

duration.pop(0)
duration.append(0.5)

pg.mixer.init()
pg.init()

pg.mixer.set_num_channels(len(letter_notes))

def play_notes(notePath, duration, duration1):

    global x
    
    print(f"{x+1} out of {len(letter_notes)}", end="\r") # To see which note is now playing
    time.sleep(duration) # make a pause 
    pg.mixer.Sound(notePath).play()
    time.sleep(duration1) # Let the sound play
    x += 1

path  = f'{__file__.removesuffix(os.path.basename(__file__))}Sounds\\'

th = {}
x = 0
for t in letter_notes:
	th[t] = Thread(target = play_notes, args = (path+'{}.ogg'.format(t), 0.1, duration[x]))
	# These are arguments (path+'{}.ogg'.format(t),0.4)
	# Lets start the thread
	th[t].start()
	th[t].join()

print()