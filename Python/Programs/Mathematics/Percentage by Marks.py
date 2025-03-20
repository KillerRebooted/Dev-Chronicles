from time import sleep
from os import system

clear = lambda:system("cls")

clear()

def LbL(Sentence, Time):

    x = len(Sentence)
    Loop = -1

    while x!=0:
        Loop += 1
        print(Sentence[Loop], end = "", flush=True)
        sleep(Time)
        x -= 1

    return ""

Choice = ""

while (Choice != "y") and (Choice != "n"):

    Choice = input("Do You Want to Skip useless Animations? This will also mean You won't be able to Read any Sentences and the Program would get straight to the Point. (y/n): ")

    if (Choice != "y") and (Choice != "n"):

        print()
        print("I told you to Type y/n, don't you know how to Read?")
        sleep(4)
        clear()
        print("I will ask You again")
        sleep(2)
        clear()

    clear()
    
if Choice == "y":
    Anim_Time = 0

else:
    Anim_Time = 0.1

Greetings = "Hello Hooman, so You are also here to get the Prophecy, you want to know your Percentage I see, My All Seeing Eye knows Everything."

print(LbL(Greetings, Anim_Time))

if Choice == "y":    
    sleep(0)
else:
    sleep(2)

clear()

NoS_Q = "How many Subjects do You Study? "

NoS = int(input(LbL(NoS_Q, Anim_Time)))

clear()

Marks = []
MM = []
Subject = []

LbL("Type Your Obtained Marks and Total Marks separated by a (.) and Subject separated by a (,), for eg.- 93 out of 100 in English would be '93.100,English' or '93.100,Eng'", Anim_Time)

if Choice == "y":    
    sleep(10)
else:
    sleep(2)

clear()

for Sub in range(1, NoS+1):
    
    if str(Sub)[-1] == "1":
        Suffix = "st"

    elif str(Sub)[-1] == "2":
        Suffix = "nd"

    elif str(Sub)[-1] == "3":
        Suffix = "rd"
    
    else:
        Suffix = "th"

    Marks_Q = f"Enter Your Marks in the {Sub}{Suffix} Subject: "

    Marks_Loop = input(LbL(Marks_Q, Anim_Time))

    Decimal = Marks_Loop.index(".")
    Subj_Index = Marks_Loop.index(",")

    Marks.append(int(Marks_Loop[:Decimal]))
    MM.append(int(Marks_Loop[Decimal+1:Subj_Index]))
    Subject.append(Marks_Loop[Subj_Index+1:])

clear()

SerialNo_Marks = 0

for SerialNo in range(1, NoS+1):
    
    print(f"You got {Marks[SerialNo_Marks]} out of {MM[SerialNo_Marks]} which totals to {str((Marks[SerialNo_Marks]/MM[SerialNo_Marks]) * 100)}% in {Subject[SerialNo_Marks]}")

    SerialNo_Marks += 1

    sleep(0.5)

Total_Marks = 0
Total_MM = 0

SerialNo_Marks = 0

for SerialNo in range(1, NoS+1):

    Total_Marks += Marks[SerialNo_Marks]
    Total_MM += MM[SerialNo_Marks]

    SerialNo_Marks += 1

print()
print(f"You Scored {(Total_Marks/Total_MM) * 100}% in Total")