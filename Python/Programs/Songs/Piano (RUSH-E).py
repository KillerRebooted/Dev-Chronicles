RUSH_E = [
			
			'e4','e4','e4','e4','e4','e4','e4', 'e4','e4','e4','e4','e4','e4','e4', 'e4','e4','e4','e4','e4','e4','e4', 'f4','e4','d-4','e4',

			'a4', 'c5', 'd5', 'd5', 'd5', 'd5', 'd5', 'c5', 'b4', 'd5', 'c5', 'c5', 'c5', 'c5', 'c5', 'b4', 'a4', 'c5', 'b4', 'b4', 'b4', 'b4',

			'f-4', 'b4', 'g-4',

			'e4','e4','e4','e4','e4','e4','e4', 'e4','e4','e4','e4','e4','e4','e4',
				
			'e4', 'e4', 'e4', 'f4', 'e4', 'd-4', 'e4',

			'a4', 'c5', 'e5', 'a5', 'c6', 'd6', 'c6', 'b5', 'd6', 'c6', 'b5', 'a5', 'c6',

			'b5', 'a5', 'g-5', 'b5', 'a5', 'e5', 'c5', 'a4', 'f5', 'e5', 'd5', 'c5', 'b4', 'a4', 'g-4', 'b4', 'a4'
			
			]

Duration = [
			
			0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1,
			
			0.1, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0.1, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
			
			0, 0, 0, 0, 0, 0, 0.1,

			0, 0, 0.1, 0.1, 0.3, 0, 0, 0, 0, 0, 0, 0, 0,

			0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.9
			
			]

from threading import Thread
import pygame as pg 
import time

pg.mixer.init()
pg.init()

pg.mixer.set_num_channels(len(RUSH_E))

def play_notes(notePath,duration, duration1):

	global x
	print(notePath) # To see which note is now playing
	time.sleep(duration) # make a pause 
	pg.mixer.Sound(notePath).play()
	time.sleep(duration1) # Let the sound play 
	x += 1

path  = f'{__file__.replace("Piano (RUSH-E).py", "")}Sounds\\'

th = {}
x = 0
for t in RUSH_E:
	th[t] = Thread(target = play_notes, args = (path+'{}.ogg'.format(t),0.1,Duration[x]))
	# These are arguments (path+'{}.ogg'.format(t),0.4)
	# Lets start the thread
	th[t].start()
	th[t].join()