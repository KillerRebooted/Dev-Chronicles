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

driver.get("https://humanbenchmark.com/tests/reactiontime")

driver.maximize_window()

driver.find_element(By.XPATH, f"//h1[text()='Reaction Time Test']").click()
target = driver.find_element(By.XPATH, f"//div[@class='view-waiting css-yg2dtu']")

while True:

    try:
        if target.get_attribute("class") == "view-go css-yg2dtu":
            target.click()
            time.sleep(0.5)
            target.click()
    except:
        break

while True:
    time.sleep(5)