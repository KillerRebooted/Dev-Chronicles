from time import sleep
import random
from os import system

Prime_Numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

clear = lambda: system("cls")

clear()

Option = "Invalid Option"

while Option == "Invalid Option":
    
    Tutorial = input("Do You want a Tutorial? (yes/no): ")

    if Tutorial == "no":
    
        clear()
        print("I Guess You have Played this Game Earlier.")
        sleep(2)
        clear()

        Option = "Valid Option"

    elif Tutorial == "yes":

        clear()

        print("This is A Number Guessing Game.")
        sleep(2)
        print()
        print("""You have to Choose a Difficulty:

a) 10 : The Computer will Choose a Number from 0-10.
b) 100 : The Computer will Choose a Number from 0-100.
c) 1000 : The Computer will Choose a Number from 0-1000.""")

        sleep(6)
        print()
        print("And You have to Guess the Number based on some Clues.")
        sleep(3)

        clear()

        Option = "Valid Option"

    else:
    
        clear()
        print("Invalid Option")
        sleep(1)
        clear()

Difficulty = int(input("Choose the Difficulty (10, 100, 1000): "))

clear()

Number = random.randint(1, Difficulty)

Guess = None

if Difficulty == 10:
    
    Tries = 2
    print("You Chose the Easy Difficulty", end="\r")
    sleep(1)
    print("You Chose the Easy Difficulty, NOOB!")
    sleep(2)
    clear()

if Difficulty == 100:

    Tries = 5
    print("You Chose the Medium Difficulty.")
    sleep(2)
    clear()

if Difficulty == 1000:

    Tries = 10
    print("You Chose the Nightmare Difficulty. G-", end="\r")
    sleep(0.5)
    print("You Chose the Nightmare Difficulty. G-G-", end="\r")
    sleep(0.5)
    print("You Chose the Nightmare Difficulty. G-G-Good Luck")
    sleep(2)
    clear()

while Guess != Number:

    if Number in Prime_Numbers:

        Rand_Number_Div = Number

    else:
        
        Rand_Number_Div = random.randint(2, Number-1)

        while (Number % Rand_Number_Div != 0):

            Rand_Number_Div = random.randint(2, Number-1)
    
    Rand_Number_Mul = random.randint(3, 9)
    Predecessor = random.randint(1, Number)
    Successor = random.randint(Number, Difficulty)

    if Tries <= 0:

        print("You Lost")
        sleep(2)
        print()
        print(f"The Number was {Number}")
        print()
        quit()

    Range = print(f"The Number is between {Predecessor} and {Successor}")

    if Rand_Number_Div == Number:

        Multiply = print(f"{Number * Rand_Number_Mul} is a Multiple of the Number")
        Hint = [Range, Multiply]

        print (random.sample(Hint, 1))
        print("The Number is a Prime Number")

    if Rand_Number_Div != Number:

        Divide = print(f"{Rand_Number_Div} is a Factor of the Number")
        Multiply = print(f"{Number * Rand_Number_Mul} is a Multiple of the Number")

        Hint = [Divide, Range, Multiply]
        print (random.sample(Hint, 1))

    print()
    Guess = int(input(f"Guess ({Tries} Tries Left): "))
    print()

    Tries -= 1

print()
print("You Won!")
print(f"The Number was {Number}")
print()