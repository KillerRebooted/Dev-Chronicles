import os, time, keyboard

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

driver.get("https://humanbenchmark.com/tests/verbal-memory")

driver.maximize_window()

time.sleep(1)

driver.find_element(By.XPATH, f"//button[@class='css-de05nr e19owgy710' and text()='Start']").click()

words = set()

seen = driver.find_element(By.XPATH, f"//button[text()='SEEN']")
new = driver.find_element(By.XPATH, f"//button[text()='NEW']")

exit = False
while not exit:

    word = driver.find_element(By.CLASS_NAME, "word").text

    try:

        if keyboard.is_pressed("escape"):
            exit = True

        if word not in words:
            new.click()
        else:
            seen.click()

    except:

        exit = True

    words.add(word)

while True:
    time.sleep(5)