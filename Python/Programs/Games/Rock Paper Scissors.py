import random
from os import system
from time import sleep
import subprocess
import sys
import os

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gTTS', 'pyttsx3', 'playsound'])

import gtts
from playsound import playsound

Computer = random.choice("rps")

speech = gtts.gTTS("चलिये शुरू करते हैं", lang = "hi", tld = "co.in", slow = False)
speech.save("Speech.mp3")

clear = lambda: system("cls")

clear()

print("Welcome to Rock, Paper, Scissors")
sleep(2)
print()
print("You must already know the Rules")

playsound("Speech.mp3")
os.remove("Speech.mp3")

clear()

Player = input("Rock, Paper, Scissors (r/p/s): ")

if Player == ('r') or ('p') or ('s'):
    
    if Player == "r":

        Player = "Rock"

    elif Player == "p":

        Player = "Paper"

    elif Player == "s":

        Player = "Scissors"

    print()
    print(f"Player: {Player}")
    print()

    if Computer == "r":

        Computer = "Rock"

    elif Computer == "p":

        Computer = "Paper"

    elif Computer == "s":

        Computer = "Scissors"

    print(f"Computer: {Computer}")

    if Player == Computer:

        print()
        print("Tie")

    elif Player == "Rock" and Computer == "Scissors":

        print()
        print("Player Wins")

    elif Player == "Paper" and Computer == "Rock":

        print()
        print("Player Wins")

    elif Player == "Scissors" and Computer == "Paper":

        print()
        print("Player Wins")

    elif Computer == "Rock" and Player == "Scissors":

        print()
        print("Computer Wins")

    elif Computer == "Paper" and Player == "Rock":

        print()
        print("Computer Wins")

    elif Computer == "Scissors" and Player == "Paper":

        print()
        print("Computer Wins")

    print()

else:

    print("Invalid Option")