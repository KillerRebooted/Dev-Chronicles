from time import sleep
from os import system

clear = lambda: system("cls")

clear()

Table = int(input("What Table do You want to Practice (Enter a Number): "))
Times = int(input("Enter the Number till which You want to Practice: "))

Correct = []
Wrong = []
Wrong_Num = []

clear()

for i in range(1, Times+1):

    Ans = int(input(f"{Table} X {i} = "))

    if Ans == Table*i:

        Correct.append(Ans)

    else:

        Wrong.append(Ans)
        Wrong_Num.append(i)

clear()

if len(Wrong) != 0:

    print(f"You got {len(Correct)} Correct and {len(Wrong)} Wrong.")
    sleep(2)

    print()
    print("The Ones that You got Wrong were: ")
    print()
    
    for i in range(1, len(Wrong)+1):

        print(f"Wrong (Your Choice): {Table} X {Wrong_Num[i-1]} = {Wrong[i-1]}")
        print(f"Correct: {Table} X {Wrong_Num[i-1]} = {Table*Wrong_Num[i-1]}")
        print()

        sleep(1)

else:

    print(f"You got all {len(Correct)} Correct. Congratulations!")