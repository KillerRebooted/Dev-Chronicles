from os import system

clear = lambda: system("cls")

clear()

Numbers1 = input("Enter the Numbers separated by commas: ").split(",")
Numbers2 = []

for i in Numbers1:

    if i.strip().isdigit() == False:

        print()
        raise Exception("Baka\n")

for i in Numbers1:

    Numbers2.append(int(i.strip()))

x = 0

for i in range(min(Numbers2), 0, -1):

    for j in Numbers2:

        if j % i == 0:

            x += 1

        else:

            x = 0
            break

    if len(Numbers2) == x:

        print(f"\nThe HCF of the Number(s) {str(Numbers2).replace('[', '').replace(']', '')} is \033[1m{i}\033[0m\n")
        break