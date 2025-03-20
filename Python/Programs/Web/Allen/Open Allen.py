import os

os.system("pip install pyautogui")

import pyautogui
from time import sleep
import webbrowser

clear = lambda: os.system("cls")

clear()

webbrowser.open("https://student.allenbpms.in/Login?ReturnUrl=%2F")

sleep(10)
pyautogui.press("tab")
pyautogui.write("1000534177")
pyautogui.press("tab")
pyautogui.write("0d771c5")
pyautogui.press("tab")
pyautogui.press("enter")
sleep(2)
pyautogui.press("tab", presses=3)
pyautogui.press("enter")
sleep(6)

pyautogui.press("tab", presses=7)

pyautogui.press("enter")
