import datetime
import os
import time
import pyautogui

def send_message(receivers:list, messages:list, paste:list=[False], target_time:list=None, shutdown:bool=False):

    target_time = target_time               #Time in 24-Hour Format
    receivers = receivers                   #List of Receivers
    messages = messages                     #String List
    paste = paste                           #[False, [2, 4]] : Boolean to specify whether to paste the most recent item from clipboard. Tuple specifies on which message index to paste.

    while True:

        time.sleep(1)

        dt = datetime.datetime.now()

        if (target_time == None) or (dt.hour == target_time[0] and dt.minute == target_time[1] and dt.second == target_time[2]):
            
            for receiver in receivers:

                os.system("TASKKILL /F /IM whatsapp.exe")
                time.sleep(2)
                os.startfile("C:/Program Files/WindowsApps/5319275A.WhatsAppDesktop_2.2436.6.0_x64__cv1g1gvanyjgm/WhatsApp.exe") #Replace with the WhatsApp.exe location on your Computer
                time.sleep(2)
                pyautogui.write(receiver)
                time.sleep(2)
                pyautogui.press("tab")
                pyautogui.press("enter")
                time.sleep(1)

                iter = 1

                for message in messages:
                    
                    if (paste[0]) and (iter in paste[1]):
                        pyautogui.hotkey("ctrl", "v")
                        time.sleep(0.5)
                    
                    pyautogui.write(message, interval=0.01)
                    pyautogui.press("enter")
                    time.sleep(0.5)

                    iter += 1

            else:

                break
    
    os.system(f"TASKKILL /F /IM whatsapp.exe")
    if shutdown:
        os.system("shutdown /s /t 0")