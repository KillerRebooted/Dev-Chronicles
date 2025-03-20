import os, time

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

driver.get("https://humanbenchmark.com/tests/memory")

driver.maximize_window()

driver.find_element(By.XPATH, "//button[normalize-space()='Start']").click()

time.sleep(1)

level = 1

while True:

    buttons = []

    while len(buttons) != (level+2):

        try:
            buttons = driver.find_elements(By.CSS_SELECTOR, "div[class='active css-lxtdud eut2yre1']")
        except:
            pass

    time.sleep(2)

    try:
        for i in buttons:
            i.click()
    except:
        break

    level += 1

while True:
    time.sleep(5)