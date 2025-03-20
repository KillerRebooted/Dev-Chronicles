import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    
    import os
    from os import system

    Steam = input("Steam: ")
    Vanguard = input("Vanguard: ")
    Driver_Assistant = input("Driver Assistant: ")
    Epic_Games = input("Epic Games: ")

    clear = lambda: system("cls")

    clear()

    if Steam == "y":
    
        os.system("TASKKILL /F /IM steam.exe")

    if Vanguard == "y":

        os.system("TASKKILL /F /IM vgtray.exe")

    if Driver_Assistant == "y":
        
        os.system("TASKKILL /F /IM DSATray.exe")

    if Epic_Games == "y":
        
        os.system("TASKKILL /F /IM EpicGamesLauncher.exe")

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)