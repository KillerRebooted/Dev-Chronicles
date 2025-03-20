from os import system

clear = lambda: system('cls')

clear()

print()

Number = int(input("Please Enter the Number: "))

print()

NewNumber = Number

while True:

    while Number != 1:

        if Number % 2 == 0:
        
            Number /= 2

        else:

            Number = 3 * Number + 1

    NewNumber += 1
    Number = NewNumber
    print(Number)