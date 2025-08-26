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

driver.get('https://www.arealme.com/colors/en/')

driver.maximize_window()

time.sleep(2)

driver.find_element(By.XPATH, f'//button[normalize-space()="Start"]').click()

while True:    

    try:

        list = driver.find_element(By.CLASS_NAME, "patra-color").find_elements(By.CSS_SELECTOR, "div span")
    
        colors = []
    
        for i in range(3):
    
            colors.append(list[i].value_of_css_property("background-color"))
    
        for i in colors:
    
            if colors.count(i) == 1:
        
                list[colors.index(i)].click()
                clicked = True
    
                break
    
        else:
    
            main_color = i
            clicked = False
    
        if clicked:
    
            continue
        
        for i in list:
        
            if i.value_of_css_property("background-color") != main_color:
    
                i.click()
                break

    except:
        break

while True:
    time.sleep(5)