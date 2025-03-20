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

driver.get('https://www.arealme.com/1-to-50/en/')

driver.maximize_window()

time.sleep(1)

driver.find_element(By.XPATH, f"//span[@class='s0_d round']").click()
time.sleep(0.1)
driver.find_element(By.XPATH, f"//span[@class='content' and text()='Start']").click()

n = 1

# Find the element using text
while n != 51:    
    
    driver.find_element(By.XPATH, f"//div[@class='dp-box-text' and text()='{n}']").click()
    n += 1

while True:
    time.sleep(5)