import os, time, pyautogui

clear = lambda: os.system("cls")

clear()

try:

    from selenium import webdriver

    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By

except:
    
    os.system("pip install selenium")
    os.system("pip install webdriver-manager")

    from selenium import webdriver

    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service())

driver.get("https://humanbenchmark.com/tests/typing")

driver.maximize_window()

time.sleep(1)

pyautogui.PAUSE = 0

paragraph = driver.find_elements(By.CLASS_NAME, "incomplete")

paragraph_text = "".join([i.text if i.text != "" else " " for i in paragraph])

pyautogui.write(paragraph_text)

while True:
    time.sleep(5)