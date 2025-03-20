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

driver.get("https://humanbenchmark.com/tests/aim")
action = webdriver.common.action_chains.ActionChains(driver)

driver.maximize_window()

while True:

    try:
        target = driver.find_element(By.XPATH, f"//div[@class='css-q4kt6s e6yfngs1']")
        action.move_to_element(target).click().perform()

    except:
        break

while True:
    time.sleep(5)