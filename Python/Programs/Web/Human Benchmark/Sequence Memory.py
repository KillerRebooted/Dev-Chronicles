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

driver.get("https://humanbenchmark.com/tests/sequence")

driver.maximize_window()

time.sleep(2)

driver.find_element(By.XPATH, f'//button[normalize-space()="Start"]').click()

level = 1
boxes = []

list = driver.find_element(By.CLASS_NAME, "squares").find_elements(By.CSS_SELECTOR, "div div")

exit = False
while not exit:

    for i in list:
        if i.get_attribute("class") == "square active":
            
            if not boxes:
                boxes.append(i)
            elif boxes[-1] != i:
                boxes.append(i)

    if len(boxes) == level:

        time.sleep(3)

        for i in boxes:
            try:
                i.click()
            except:
                exit = True
                break

        level += 1
        boxes = []

while True:
    time.sleep(5)