from os import system

clear = lambda: system('cls')

clear()

num = input("Enter the Number till which you want the Series to be printed (>= 2): ")

if (num.isdigit() == False) or (int(num) < 2):

    print()
    raise Exception("Baka\n")

a = 0
b = 1

print(f"\n{1}\n{1}")

for i in range(int(num)-2):

    a, b = b, a+b
    print(a+b)

print()