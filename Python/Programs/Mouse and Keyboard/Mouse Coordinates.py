from os import system
from time import sleep

try:

    import mouse

except:

    system('pip install mouse')

    import mouse

clear = lambda: system("cls")

while True:
    
    sleep(1)

    while mouse.is_pressed("left") == True:
        sleep(0.5)
        print(mouse.get_position())