AMONG_US_DRIP = [

			'c2', 'c5', 'd-5', 'f5', 'f-5', 'f5', 'd-5', 'c5', 'a-4', 'd5', 'c5',

			'g1', 'c2', 'c5', 'd-5', 'f5', 'f-5', 'f5', 'd-5', 'f-5',

			'f-5', 'c2', 'f5', 'd-5', 'f-5', 'c3', 'f5', 'd-5', 'c3', 'c2', 'c5', 'd-5', 'f5', 'f-5', 'c3', 'c2', 'f5',

			'd-5', 'c5', 'c3', 'c2', 'a-4', 'd5', 'c5', 'c4', 'c3', 'a-3', 'a-2', 'g3', 'g2', 'c3', 'c2', 'c5', 'd-5',

			'f5', 'f-5', 'd-3', 'd-2', 'f5', 'd-5', 'f-5', 'f-3', 'f-2', 'f-3', 'f-2', 'f-3', 'f-2', 'f-5', 'f5', 'f-3', 'f-2', 'f-3', 'f-2', 'd-5', 'f-5', 'f-3', 'f-2', 'f5', 'f-3', 'f-2', 'd-5', 'c3', 'c2'

			]

Duration = [

			0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,

			0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,

			0.1, 0, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0, 0.1, 0.1, 0.1, 0.1, 0, 0, 0.1,

			0.1, 0.1, 0, 0, 0.1, 0.1, 0.1, 0.1, 0, 0.1, 0, 0, 0, 0.1, 0, 0.1, 0.1,

			0.1, 0.1, 0, 0, 0.1, 0.1, 0.1, 0, 0, 0.1, 0, 0.1, 0, 0.1, 0.1, 0, 0, 0, 0, 0.1, 0.1, 0, 0, 0.1, 0.1, 0, 0.1, 0.1, 0

			]

Duration1 = [
			
			0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0, 0, 0.5,

			0.1, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.7,

			0, 0, 0.1, 0, 0, 0, 0.1, 0, 0, 0.3, 0.1, 0.1, 0.1, 0, 0, 0.1, 0.1,

			0.1, 0, 0, 0.5, 0, 0, 0.1, 0, 0.2, 0, 0, 0, 0.1, 0, 0.3, 0.1, 0.1,

			0.1, 0, 0, 0.1, 0.1, 0.1, 0, 0, 0.3, 0, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3

			]

from threading import Thread
import pygame as pg 
import time

pg.mixer.init()
pg.init()

pg.mixer.set_num_channels(len(AMONG_US_DRIP))

def play_notes(notePath,duration, duration1):

	global x
	print(notePath) # To see which note is now playing
	time.sleep(duration) # make a pause 
	pg.mixer.Sound(notePath).play()
	time.sleep(duration1) # Let the sound play 
	x += 1

path  = f'{__file__.replace("Piano (AMONG US DRIP).py", "")}Sounds\\'

th = {}
x = 0
for t in AMONG_US_DRIP:
	th[t] = Thread(target = play_notes, args = (path+'{}.ogg'.format(t),Duration[x],Duration1[x]))
	# These are arguments (path+'{}.ogg'.format(t),0.4)
	# Lets start the thread
	th[t].start()
	th[t].join()