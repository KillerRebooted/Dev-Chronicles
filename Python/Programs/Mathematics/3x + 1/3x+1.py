from os import system

clear = lambda: system('cls')

clear()

print()

Number = int(input("Please Enter the Number: "))

print()

x = 0

while Number != 1:

    if Number % 2 == 0:
    
        Number /= 2

        x += 1

        print(f"{Number*2} / 2 = {Number}")

    else:

        Number = 3 * Number + 1

        x += 1

        print(f"3 * {(Number-1)/3} + 1 = {Number}")

print()
print(x, " Steps")
print()