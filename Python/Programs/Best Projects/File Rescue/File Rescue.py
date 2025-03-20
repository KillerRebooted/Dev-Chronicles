import os, sys, subprocess
from os import system

clear = lambda: system("cls")

clear()

if os.path.isdir(f"{__file__.removesuffix(os.path.basename(__file__))}File Rescue Cache"):

    pass

else:

    os.mkdir(f"{__file__.removesuffix(os.path.basename(__file__))}File Rescue Cache")

with open(f"{__file__.removesuffix(os.path.basename(__file__))}File Rescue Cache\\cache.txt", "a+") as file:

    pass

with open(f"{__file__.removesuffix(os.path.basename(__file__))}File Rescue Cache\\cache.txt", "r") as file:

    content = file.readlines()
    new_content = {}

    for i in content:

        new_content[i[ : i.find("-") - 1]] = int(i[i.find("-") + 2 : ].removesuffix("\n"))

    content = new_content

if len(content) == 0:

    Cache = {}

    sp_to_get_drives = subprocess.Popen('wmic logicaldisk get DeviceID ',shell=True,stdout=subprocess.PIPE,text=True)
    x = (sp_to_get_drives.stdout.read()).split(" ")

    Drives=[]

    for i in x:
        if ":" in i:
            Drives.append(i.strip("\n"))

    Cache["Total Files"] = 0

    print("It only Happens the First Time\nPlease wait patiently as it may take upto 5 minutes\nBuilding Cache Files...")

    for i in Drives:

        Cache[i] = sum([len(Files) for r, d, Files in os.walk(f"{i}\\")])

        Cache["Total Files"] += Cache[i]

    with open(f"{__file__.removesuffix(os.path.basename(__file__))}File Rescue Cache\\cache.txt", "w+") as file:

        for drive in Drives:

            file.write(f"{drive} - {Cache[drive]}\n")

        file.write(f"Total Files - {Cache['Total Files']}")

elif len(content) != 0:

    Location = input("Enter the Search Location ('full' for Searching the Whole Computer): ")
    Key_Word = input("Enter the Key Word to look for: ")

    Total_Files = content["Total Files"]

    clear()

    if Location == "full":

        Drives = []

        for i in content:

            Drives.append(i)

        Drives.pop(-1)

        for drive in Drives:

            if os.path.exists(f"{drive.strip().upper()}\\"):

                pass

            else:

                print(f"Drive {drive.strip().upper()} not Found")
                quit()

        Total_Files = content["Total Files"]

        new_values = []

        Files_Found = 0
        i = 0

        for drive in Drives:

            drive_file_count = 0

            for root, dirs, files in os.walk(f"{drive}\\"):

                for filename in files:

                    if i > Total_Files:

                        Total_Files += 1

                    Check_File = os.path.join(root, filename)

                    Percentage_Bar = f"[{'='*round(i/Total_Files * 100)}{' '*(100 - (round(i/Total_Files * 100)))}] {round(i/Total_Files * 100)}% ({i} of {Total_Files})"

                    print(Percentage_Bar, end="\r")

                    if Key_Word.lower() in Check_File.lower():
                    
                        sys.stdout.write("\033[F")
                        print(Check_File + " "*(len(Percentage_Bar) - len(Check_File)))

                        Files_Found += 1

                        print(" "*len(Percentage_Bar))
                        print()
                        sys.stdout.write("\033[F")

                    i += 1
                    drive_file_count += 1

            new_values.append(drive_file_count)

        Cache = {}
        Cache["Total Files"] = 0

        for i, j in enumerate(Drives):
            
            Cache[Drives[i]] = new_values[i]
            Cache["Total Files"] += Cache[Drives[i]]

        with open(f"{__file__.removesuffix(os.path.basename(__file__))}File Rescue Cache\\cache.txt", "w+") as file:

            for drive in Drives:

                file.write(f"{drive} - {Cache[drive]}\n")

            file.write(f"Total Files - {Cache['Total Files']}")

    else:

        Files_Found = 0
        i = 0

        try:

            Total_Files = content[Location.removesuffix("\\").upper()]
            is_drive = True

        except KeyError:

            Total_Files = sum([len(Files) for r, d, Files in os.walk(Location)])
            is_drive = False

        for root, dirs, files in os.walk(Location):
        
            for filename in files:

                if i > Total_Files:

                    Total_Files += 1
            
                Check_File = os.path.join(root, filename)

                Percentage_Bar = f"[{'='*round(i/Total_Files * 100)}{' '*(100 - (round(i/Total_Files * 100)))}] {round(i/Total_Files * 100)}% ({i} of {Total_Files})"

                print(Percentage_Bar, end="\r")

                if Key_Word.lower() in Check_File.lower():
                
                    sys.stdout.write("\033[F")
                    print(Check_File + " "*(len(Percentage_Bar) - len(Check_File)))

                    Files_Found += 1

                    print(" "*len(Percentage_Bar))
                    print()
                    sys.stdout.write("\033[F")

                i += 1

        Total_Files = i

        if is_drive:

            content['Total Files'] += (Total_Files - content[Location.removesuffix("\\").upper()])

            content[Location.removesuffix("\\").upper()] = Total_Files

        with open(f"{__file__.removesuffix(os.path.basename(__file__))}File Rescue Cache\\cache.txt", "w+") as file:

            for i in content:

                file.write(f"{i} - {content[i]}\n")

    print(f"[{'='*100}] {100}% ({Total_Files} of {Total_Files} Files)")
    print(f"\n{Files_Found} Files with Key Word '{Key_Word}' Found\n")

os.system("pause")