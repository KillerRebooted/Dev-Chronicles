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

driver.get('https://www.arealme.com/odd-one-out/en/')

driver.maximize_window()

time.sleep(1)

driver.find_element(By.XPATH, f'//button[normalize-space()="Start"]').click()

n = 62

# Find the button using text
while n != 0:

    driver.find_element(By.XPATH, f"//div[@data-odd='true']").click()

    n -= 1

while True:
    time.sleep(5)
