from os import system
from time import sleep

clear = lambda: system("cls")

def LbL(Sentence, Time):

    x = len(Sentence)
    Loop = -1

    while x!=0:
        Loop += 1
        print(Sentence[Loop], end = "", flush=True)
        sleep(Time)
        x -= 1

    return ""

def Options(Question, Option1, Option2):

    Discipline = False

    while (Discipline == False):

        clear()    
        
        LbL(Question, 0.1)
        sleep(1)
    
        print("\n")
    
        print(f"""1. {Option1}
2. {Option2}""")

        print()
        
        Option_Chosen = input("You Chose [1/2]: ")

        if (Option_Chosen == "1") or (Option_Chosen == "2"):

            Discipline = True
        
    if Option_Chosen == "1":

        clear()
        
        r = 255
        g = 255
        b = 255

        print(Question)
        print()

        while g != 0 and b != 0:

            print(f"\033[38;2;{r};{g};{b}m1. {Option1} \033[38;2;255;255;255m", end="\r")
            
            g -= 15
            b -= 15
            sleep(0.1)
            
        sleep(1)

    if Option_Chosen == "2":

        clear()
        
        r = 255
        g = 255
        b = 255

        print(Question)
        print()

        while g != 0 and b != 0:

            print(f"\033[38;2;{r};{g};{b}m2. {Option2} \033[38;2;255;255;255m", end="\r")
            
            g -= 15
            b -= 15
            sleep(0.1)
            
        sleep(1)

Options("You...", "Run!", "Confront the Man")