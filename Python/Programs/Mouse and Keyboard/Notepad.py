from time import sleep
import pyautogui
import os

os.startfile("notepad")
sleep(1)
pyautogui.write("Hello Person", interval=0.1)