import os, pyautogui, numpy, time
from mss import mss
from PIL import Image

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

driver.maximize_window()

pyautogui.PAUSE = 0

color = [149,195,232]
quit_color = [255,209,84]

monitor = {"top": 225, "left": 510, "width": 900, "height": 480}
output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

time.sleep(1)
    
with mss() as ss:

    img = ss.grab(monitor)

    pillow = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")

    im = numpy.array(pillow)

    y, x = numpy.where(numpy.all(im==color, axis=2))

    coords = (x[len(x)//2]+monitor["left"], y[len(y)//2]+monitor["top"])

    pyautogui.click(coords)

    check_element = driver.find_element(By.XPATH, f"//span[@class='css-yuq7ce']")

    while True:
        
        img = ss.grab(monitor)

        pillow = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")

        im = numpy.array(pillow)

        y, x = numpy.where(numpy.all(im==color, axis=2))

        coords = (x[len(x)//2]+monitor["left"], y[len(y)//2]+monitor["top"])

        pyautogui.click(coords)
        
        try:
            check_element.text
        except:
            break

while True:
    time.sleep(5)