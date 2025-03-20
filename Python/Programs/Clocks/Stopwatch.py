import threading
from time import sleep
from os import system
import keyboard

clear = lambda: system('cls')

clear()

print("Press SPACE to Stop\n")

Running = True

def stop():

    global Running

    while True:

        if keyboard.is_pressed("space"):

            Running = False
            print()
            break

def stopwatch():

    global prefix1, prefix2

    min = 0
    sec = -1

    st.start()
    
    while Running:

        sleep(1)
        sec += 1

        if min < 10:
            prefix1 = 0

        else:
            prefix1 = ""

        if sec < 10:
            prefix2 = 0

        else:
            prefix2 = ""

        if sec == 60:

            sec = 0
            min += 1

        print(f"{prefix1}{min}:{prefix2}{sec}", end="\r")

sw = threading.Thread(target=stopwatch)
st = threading.Thread(target=stop)

sw.start()