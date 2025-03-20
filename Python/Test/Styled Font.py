from cfonts import render
from time import sleep
from os import system
import time

def Big_Text(Text, Time):

    clear = lambda: system("cls")

    x = 0
    y = 0

    color1 = ["red", "yellow", "green", "blue", "cyan", "magenta"]
    color2 = ["blue", "magenta", "red", "yellow", "green", "cyan"]

    t_end = time.time() + Time

    Text = Text.split()

    z = 0

    Txt = ""

    while time.time() < t_end:

        clear()

        if Txt.split() != Text:

            Txt = Txt + f" {Text[z]}"

        else:

            Txt = Txt

        if x == len(color1):

            x = 0
            y = 0

        output = render(Txt, colors=[color1[x], color2[y]], align='center')
        print(output)

        if z < len(Text)-1:
        
            z += 1

        else:

            z += 0

        x += 1
        y += 1

        sleep(1)

Big_Text("Hello Fellow User", 5)