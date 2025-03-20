from math import ceil
import os, sys
from os import system
import pandas as pd
from time import sleep

#Challenge: Find more than 1 Error

clear = lambda:system("cls")

class color:
   
   BOLD = '\033[1m'
   END = '\033[0m'
   YELLOW = '\033[93m'

def inp(Variable, Sentence, Exception):

    global a

    a = {}
    
    x = "0"

    while x not in Exception:

        x = input(Sentence)

        if x not in Exception:

            sys.stdout.write("\033[F")
            print(" "*len(Sentence + x))
            sys.stdout.write("\033[F")

    a[Variable] = x

    return ""

size = os.get_terminal_size()
columns = size.columns

if os.path.isdir(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files"):

    clear()
    
else:

    os.mkdir(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files")

if os.path.isdir(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files\Scores"):

    clear()
    
else:

    os.mkdir(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files\Scores")

if os.path.isdir(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files\Quizzes"):

    clear()
    
else:

    os.mkdir(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files\Quizzes")

Option = None

while (Option != "1") and (Option != "2") and (Option != "3") and (Option != "4"):

    clear()

    print(" Quiz Hub ".center(columns, "-"))
    print()
    print("\U0001F4BB SELECT AN OPTION \U0001F4BB". center(columns, " "))
    print()

    print("1. Make a Quiz".center(columns, " "))
    print("2. Attempt the Quiz".center(columns, " "))
    print("3. Leaderboards".center(columns, " "))
    print("4. QUIT! (Not Recommended)".center(columns, " "))
    print()

    Option = input("Choose an Option (1/2/3/4): ")

    if (Option != "1") and (Option != "2") and (Option != "3") and (Option != "4"):

        clear()

        print()
        print("I assume You wanted to Quit?")
        sleep(2)
        print("But I looked through the ", end = "", flush = True)
        sleep(1)
        print("ENTIRE ", end = "", flush = True)
        sleep(1)
        print("CODE ", end = "", flush = True)
        sleep(1)
        print("and cannot find where I asked You to type ", end = "", flush = True)
        sleep(1.5)
        print(f"'{Option}'")
        sleep(2)

#Make Quiz

if Option == "1":

    clear()
    print(" Quiz Master ".center(columns, "-"))

    print()

    print("Please make the Quiz ", end="", flush = True)
    sleep(1.5)
    print("CAREFULLY ", end="", flush = True)
    sleep(1.5)
    print("as I have not Developed an AI to Correct the Mistakes during Question Making. ", end="", flush=True)
    sleep(4)
    print("(YET!)")
    sleep(1.5)

    Running = True

    while Running:

        clear()
        print(" Quiz Master ".center(columns, "-"))
        print()
        
        FileName = input("Enter the Name of the Quiz: ")

        try:    
        
            file = open(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files\Quizzes\{FileName}.xlsx", "w+")
            file.close()
            Running = False

        except:

            print()

            print(f"A file with Name '{FileName}' already exists.")
            print()
            sleep(2)
            
            Delete = input("Are you sure you want to overwrite this file? (y/n): ")

            if Delete == "y":

                Running = False

            else:

                Running = True

    clear()
    print(" Quiz Master ".center(columns, "-"))
    print()

    Question_No = 0
    DataFrame = {}
    List_Of_Questions = []
    List_Of_Options = []

    print("""Don't type the Question No. and Type 0 to stop making Questions

Type the Questions:""")

    while True:

        Question = input(f"\n\n-> Q.{Question_No+1}. ")

        if Question == "0":

            break

        else:

            List_Of_Questions.append(Question)
            DataFrame["Questions"] = List_Of_Questions
            Question_No += 1

    clear()
    print(" Quiz Master ".center(columns, "-"))
    print()
    Question_No = 0

    print("""Type the 4 Options separated by a ~. Type 'quit' to quit.

For eg:-

Input: Hello~Bye~Hi~World

Output: A) Hello
        B) Bye
        C) Hi
        D) World""")
    
    while Question_No != len(List_Of_Questions):

        print("\n")

        Running = True

        while Running:

            Options = input(f"Q{Question_No+1}. {DataFrame['Questions'][Question_No]}\n\nEnter the Options: ")

            if (Options.count("~") != 3) or ("" in Options.split("~")):

                if Options.lower() == "quit":

                    clear()
                    quit()

                Running = True

                sys.stdout.write("\033[F" * (ceil(len(f"Q{Question_No+1}. {DataFrame['Questions'][Question_No]}")/columns)+1))

                print(" "*len(f"Q{Question_No+1}. {DataFrame['Questions'][Question_No]}"))
                print(" "*len("Enter the Options: " + Options))

                sys.stdout.write("\033[F" * (ceil(len(f"Q{Question_No+1}. {DataFrame['Questions'][Question_No]}")/columns)+2))

            else:

                Running = False

        List_Of_Options.append(Options)
        Question_No += 1

    Change = None

    while Change != "0":

        print("\n")

        Change = input(f"Do you wish to Change any Options? Type the Question No. (1-{len(DataFrame['Questions'])}). If You are satisfied with the Options, Please Type 0: ")

        if (Change.isdigit() == False) or (int(Change) not in range(1, len(DataFrame['Questions'])+1)):

            clear()

        else:

            print("\n\n")

            Change_Answer = input(f"""Q{int(Change)}. {DataFrame['Questions'][int(Change)-1]}\n\nEnter the Options: """)

            if (Change_Answer.count("~") != 3) or ("" in Change_Answer.split("~")):

                clear()

            else:

                List_Of_Options[int(Change)-1] = Change_Answer
                clear()

        print(" Quiz Master ".center(columns, "-"))
        print()

        print("""Type the 4 Options separated by a ~. Type 'quit' to quit.

For eg:-

Input: Hello~Bye~Hi~World

Output: A) Hello
        B) Bye
        C) Hi
        D) World""")

        Question_No = 0

        while Question_No != len(List_Of_Questions):

            print("\n")

            print(f"Q{Question_No+1}. {DataFrame['Questions'][Question_No]}\n\nEnter the Options: {List_Of_Options[Question_No]}")

            Question_No += 1
    
    List_Of_Options_A = []
    List_Of_Options_B = []
    List_Of_Options_C = []
    List_Of_Options_D = []

    for i in List_Of_Options:

        List_Of_Options_A.append(i.split("~")[0])
        List_Of_Options_B.append(i.split("~")[1])
        List_Of_Options_C.append(i.split("~")[2])
        List_Of_Options_D.append(i.split("~")[3])

    DataFrame["A"] = List_Of_Options_A
    DataFrame["B"] = List_Of_Options_B
    DataFrame["C"] = List_Of_Options_C
    DataFrame["D"] = List_Of_Options_D

    clear()
    print(" Quiz Master ".center(columns, "-"))
    print()
    Question_No = 0

    print("""Type the Correct Option for the Answers.
    
For eg:-

Q1 What is 2+2 ?

A) 3
B) 6
C) 4
D) I don't know

Type the Correct Option: D\n\n""")

    Correct_Answer = []

    while Question_No != len(List_Of_Questions):

        print("\n")

        print(f"""Q{Question_No+1}. {List_Of_Questions[Question_No]}

A) {List_Of_Options_A[Question_No]}
B) {List_Of_Options_B[Question_No]}
C) {List_Of_Options_C[Question_No]}
D) {List_Of_Options_D[Question_No]}""")

        print()

        inp("Correct_Answer", f"Enter the Correct Option for Question {Question_No+1}: ", "abcdABCD")

        Correct_Answer.append(a["Correct_Answer"].upper())

        Question_No += 1

    Change = None

    while Change != "0":

        print("\n")

        Change = input(f"Do you wish to Change any Answers? Type the Question No. (1-{len(DataFrame['Questions'])}). If You are satisfied with the Answers, Please Type 0: ")

        if (Change.isdigit() == False) or (int(Change) not in range(1, len(DataFrame['Questions'])+1)):

            clear()

        else:

            print("\n\n")

            Change_Answer = input(f"""Q{int(Change)}. {List_Of_Questions[int(Change)-1]}

A) {List_Of_Options_A[int(Change)-1]}
B) {List_Of_Options_B[int(Change)-1]}
C) {List_Of_Options_C[int(Change)-1]}
D) {List_Of_Options_D[int(Change)-1]}

Enter the Correct Option for Question {int(Change)}: """)

            if Change_Answer not in "abcdABCD":

                clear()

            else:

                Correct_Answer[int(Change)-1] = Change_Answer.upper()
                clear()
        
        print(" Quiz Master ".center(columns, "-"))
        print()

        print("""Type the Correct Option for the Answers.
    
For eg:-

Q1 What is 2+2 ?

A) 3
B) 6
C) 4
D) I don't know

Type the Correct Option: D\n\n""")

        Question_No = 0

        while Question_No != len(List_Of_Questions):

            print("\n")

            print(f"""Q{Question_No+1}. {List_Of_Questions[Question_No]}

A) {List_Of_Options_A[Question_No]}
B) {List_Of_Options_B[Question_No]}
C) {List_Of_Options_C[Question_No]}
D) {List_Of_Options_D[Question_No]}

Enter the Correct Option for Question {Question_No+1}: {Correct_Answer[Question_No]}""")

            Question_No += 1

    DataFrame["Answers"] = Correct_Answer

    df = pd.DataFrame(DataFrame)
    df.to_excel(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files\Quizzes\{FileName}.xlsx", sheet_name="Sheet1", index=False)

    clear()

    print(" Quiz Master ".center(columns, "-"))
    print()

    print(f"Quiz with Name '{FileName}' made Successfully!")
    print()

#Attempt Quiz

elif Option == "2":

    FileName = ""

    while os.path.exists(FileName) == False:    
        
        clear()

        Title = " Welcome to KBR Kaun Banega Roadpati "

        print(Title.center(columns, "-"))

        print()

        Quiz_Files = os.listdir(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files\Quizzes")

        for i in Quiz_Files:

            print(i.removesuffix(".xlsx"))

        print()

        #OG -> Original

        OG_FileName = input("Please Enter the Quiz Name from the above list: ")

        clear()

        OG_FileName += ".xlsx"

        FileName = __file__.removesuffix(os.path.basename(__file__)) + "Quiz Files\Quizzes\\" + OG_FileName

        if os.path.exists(FileName) == False:

            print(Title.center(columns, "-"))
            print()

            print(f"A Quiz named '{OG_FileName.removesuffix('.xlsx')}' doesn't exist.")
            
            sleep(3)

    if os.path.getsize(FileName) == 0:

        print(Title.center(columns, "-"))
        print()

        raise Exception("Trying to find an Error in my Program using Empty Files?")

    df = pd.read_excel(FileName , sheet_name='Sheet1')

    Questions = []
    A = []
    B = []
    C = []
    D = []
    Answers = []

    for i in range(len(df.index)):

        Questions.append(df.iat[i, 0])
        A.append(df.iat[i, 1])
        B.append(df.iat[i, 2])
        C.append(df.iat[i, 3])
        D.append(df.iat[i, 4])
        Answers.append(None)

    clear()

    print(Title.center(columns, "-"))

    print()

    #AuR -> Are You Ready?

    AuR = input("ARE YOU READY FOR THE QUIZ? (y/n in Upper or Lower Case): ")
    AuR_Og = AuR
    AuR = AuR.lower()

    if AuR == "y":

        clear()

        print(Title.center(columns, "-"))

        print()

        print("Alrighty", end="\r")
        sleep(0.5)
        print("Alrighty Kid", end="\r")
        sleep(0.5)

        print("Alrighty K  ", end="\r")
        sleep(0.5)
        print("Alrighty KI ", end="\r")
        sleep(0.5)
        print("Alrighty KID", end="\r")
        sleep(0.5)
        print("Alrighty \U0001F476 ")
        sleep(1.5)
        clear()

        print(Title.center(columns, "-"))

        print()

        print("Hope you are ready to face this Abomination. \U0001F62C")

    elif AuR == "n":

        clear()

        print(Title.center(columns, "-"))

        print()

        print("S", end="\r")
        sleep(0.3)
        print("Sa", end="\r")
        sleep(0.3)
        print("Sad", end="\r")
        sleep(0.3)
        print("Sad ", end="\r")
        sleep(0.3)
        print("Sad \U0001F614", end="\r")
        sleep(1.5)
        print("Sad \U0001F614, You have to take the Quiz anyways. \U0001F61C")

    else:

        clear()
        
        print(Title.center(columns, "-"))

        print()

        print(f"I don't know what '{AuR_Og}' means \U0001F914.", end="\r")
        sleep(4)
        print(f"I don't know what '{AuR_Og}' means \U0001F914. You have to take the Quiz anyways \U0001F61C")

    sleep(4)

    #QSNo -> Question Serial Number

    QSNo = 1
    QNo = 0
    x = 1
    Change = None

    while Change != "0":

        while QNo != len(df.index):
            
            clear()

            x = QSNo

            QSNo = 0
            QNo = -1

            print(Title.center(columns, "-"))

            while QNo != x-1:

                QSNo += 1
                QNo += 1

                print()
                print(f"Q{QSNo}. {Questions[QNo]}")
                print()
                print(f"""A) {A[QNo]}
B) {B[QNo]}
C) {C[QNo]}
D) {D[QNo]}

Option Chosen: {Answers[QNo]}""")

            print()
            Answer = input("What's the Answer of the Above Question (a/b/c/d in Upper or Lower Case): ")
            Answer = Answer.lower()

            if (Answer == "a") or (Answer == "b") or (Answer == "c") or (Answer == "d"):

                Answers[QNo] = Answer.upper()

                QSNo += 1
                QNo += 1

            else:
                
                clear()

                print(Title.center(columns, "-"))

                print()
                
                print("You are a Student", end="\r")
                sleep(1)
                print("You are A        ", end="\r")
                sleep(1)
                print("You are A STUDENT", end="\r")
                sleep(1)
                print("You are A STUDENT and will remain a Student", end="\r")
                sleep(1.5)
                print("You are A STUDENT and will remain a Student, OBEY", end="\r")
                sleep(1)
                print("You are A STUDENT and will remain a Student, OBEY MY ", end="\r")
                sleep(1)
                print("You are A STUDENT and will remain a Student, OBEY MY ORDERS ", end="\r")
                sleep(1)
                print("You are A STUDENT and will remain a Student, OBEY MY ORDERS and use only a/b/c/d in Upper or Lower Case.")
                sleep(5)

        clear()
        x = QSNo-1

        QSNo = 0
        QNo = -1

        print(Title.center(columns, "-"))

        while QNo != x-1:

            QSNo += 1
            QNo += 1

            print()
            print(f"Q{QSNo}. {Questions[QNo]}")
            print()
            print(f"""A) {A[QNo]}
B) {B[QNo]}
C) {C[QNo]}
D) {D[QNo]}

Option Chosen: {Answers[QNo]}""")

        print()

        if len(Questions) != 1:

            def Change_Text():

                print(f"Do you wish to Change any Answer? Type the Question No. (1-{len(Questions)}). If You are satisfied with the Answers, Please Type 0: ", end="", flush=True)

                return ""

            Change = input(Change_Text())

            print("\033[A                                                                                                                           \033[A")

        else:

            def Change_Text():

                print("Do you want to Change any Answer? Type the Question No. '1'. If You are satisfied with the Answers, Please Type 0: ", end="", flush=True)

                return ""

            Change = input(Change_Text())

            print("\033[A                                                                                                                           \033[A")

        if (Change.isdigit() == False) or (int(Change) > len(Questions)) or (int(Change) < 0):

            clear()
            print("The Mentioned Question doesn't exist.")
            print()
            print("You would have to Answer the last Question again")
            sleep(6)

        elif Change == "0":

            print()

        else:

            print()
            print("NOTE: You will have to Answer the Last Question again after changing the Answer.")
            Changed_Answer = input(f"Please Type the desired Answer for Question No. {Change} (a/b/c/d in Upper or Lower Case): ")

            if (Changed_Answer.lower() != "a") and (Changed_Answer.lower() != "b") and (Changed_Answer.lower() != "c") and (Changed_Answer.lower() != "d"):

                clear()
                print("I Hope you are not a ", end="\r")
                sleep(1)
                print("I Hope you are not a KINDER", end="\r")
                sleep(1)
                print("I Hope you are not a KINDERGARTENER", end="\r")
                sleep(1)
                print(f"I Hope you are not a KINDERGARTENER and learnt that '{Changed_Answer}' and a/b/c/d are not the same.", end="\r")
                sleep(3)

            else:

                Answers[int(Change)-1] = Changed_Answer.upper()

    Score = 0
    i = 0

    for Answer in Answers:

        if df.iat[i, 5] == Answer:

            Score += 1
        
        i += 1

    if Score == 0:

        print(f"You got {Score}/{len(Questions)}. ", end="", flush=True)
        sleep(1)
        print("ZE", end="", flush=True)
        sleep(1)
        print("RO. ", end="", flush=True)
        sleep(1)
        print("You have to Try Harder.")

    elif Score == len(Questions):

        print(f"You got {Score}/{len(Questions)}. ", end = "", flush=True)
        sleep(1)
        print("FULL ", end = "", flush=True)
        sleep(1)
        print("MARKS. ", end = "", flush=True)
        sleep(1)
        print("KEEP IT UP!")

    elif Score < (8/10)*len(Questions):

        print(f"You got {Score}/{len(Questions)}. You need to Try Harder.")

    elif (Score >= (8/10)*len(Questions)) and (Score < (9/10)*len(Questions)):

        print(f"You got {Score}/{len(Questions)}. Good going, but You could've done better.")

    else:

        print(f"You got {Score}/{len(Questions)}. KEEP IT UP!")

    sleep(3)
    print()

    for i in range(len(Questions)):

        if df.iat[i, 5] == "A":

            x = 1

        elif df.iat[i, 5] == "B":

            x = 2

        elif df.iat[i, 5] == "C":

            x = 3

        elif df.iat[i, 5] == "D":

            x = 4


        if Answers[i] == "A":

            y = 1

        elif Answers[i] == "B":

            y = 2

        elif Answers[i] == "C":

            y = 3

        elif Answers[i] == "D":

            y = 4

        print(f"Correct Answer for '{Questions[i]}' is: {df.iat[i, 5]}) {df.iat[i, x]}")
        print(f"You Chose Option: {Answers[i]}) {df.iat[i, y]}")
        print()

    Name = input("Please Enter Your Name: ")

    if Name.lower() == "shreyas":

        clear()

        if Score >= (9/10)*len(Questions):

            print(Title.center(columns, "-"))
            print()

            print("As expected ", end="", flush=True)
            sleep(1.5)
            print(f"{color.BOLD}{color.YELLOW}Lord Shreyas!{color.END}")
            sleep(3)

        else:

            print(Title.center(columns, "-"))
            print()

            print("An Honour", end="", flush=True)
            sleep(1.5)
            print(f", {color.BOLD}{color.YELLOW}Lord Shreyas!{color.END}")
            sleep(3)

    with open(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files\Scores\Scores_{OG_FileName.removesuffix('.xlsx')}.txt", "a+") as File:
            
        File.write(f"{Name} - {Score}\n")

    clear()

    print(Title.center(columns, "-"))
    print()

    print("SCORE SAVED SUCCESSFULLY")
    print()

elif Option == "3":

    Score = "x"
    Scores = os.listdir(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files\Scores")

    if Scores == []:

        clear()

        print(" Leaderboards ".center(columns, "-"))
        print()

        print("No Scores found")
        print()
        quit()

    while Score not in str(list(range(1, len(Scores)+1))):

        clear()

        print(" Leaderboards ".center(columns, "-"))
        print()

        for i in Scores:

            print(f"{Scores.index(i)+1}. {i.removeprefix('Scores_').removesuffix('.txt')}")

        print()

        Score = input("Enter the Number to see the Scores of the repective Quizzes from the above list: ")

    clear()

    print(" Leaderboards ".center(columns, "-"))
    print()

    Score_List = []

    with open(f"{__file__.removesuffix(os.path.basename(__file__))}Quiz Files\Scores\{Scores[int(Score)-1]}") as File:

        File = File.read().split("\n")
        File.pop(-1)

        if File == []:

            print("Don't try to Fool Me! This Empty File was made by You isn't it?")
            print()
            quit()

        #Separate Score

        Sep_Score = {}
        Append = ""
        x = 1

        for i in File:

            Append = ""
            
            for j in i:
                
                if j.isdigit():

                    Append += j
                
            Sep_Score[int(x)] = int(Append)
            x += 1

    Sep_Score = dict(sorted(Sep_Score.items(),key=lambda x:x[1],reverse = True))

    x = 1

    for i in Sep_Score:

        print(f"{x}. {File[i-1]}".center(columns, " "))
        x += 1

elif Option == "4":

    clear()

    print(" Quiz Hub ".center(columns, "-"))
    print()

    print("PROGRAM TERMINATED SUCCESSFULLY!")
    print()

    quit()
