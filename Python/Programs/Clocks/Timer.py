from time import sleep
from os import system
from playsound import playsound

#pip install playsound==1.2.2

clear = lambda: system("cls")

value = "Invalid Time"
Run = True

while value == "Invalid Time":

    clear()

    min = int(input("Enter the Number of Minutes (<60): "))
    sec = int(input("Enter the Number of Seconds (<60): "))

    if (min not in range(60)) or (sec not in range(60)):
        
        print()
        print(value:="Invalid Time")
        sleep(2)

    else:

        value = "Valid Time"

print()

while Run:

    if min < 10:
        prefix1 = "0"

    else:
        prefix1 = ""

    if sec < 10:
        prefix2 = "0"

    else:
        prefix2 = ""

    print(f"{prefix1}{min}:{prefix2}{sec}", end = "\r")

    sleep(1)

    if sec == 0:

        sec = 59
        
        if min == 0:
            Run = False
        
        else:
            min -= 1

    else:

        sec -= 1

print()
playsound(f"{__file__.removesuffix('Timer.py')}Alarm.mp3")