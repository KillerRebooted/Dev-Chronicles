import pyautogui
from time import sleep

Table = int(input("Table: "))
Times = int(input("Times: "))

sleep(4)

for i in range(1, Times+1):

    Ans = Table*i

    pyautogui.write(str(Ans))
    pyautogui.press("enter")