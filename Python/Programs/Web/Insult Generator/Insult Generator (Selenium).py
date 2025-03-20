from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def insult(name):

    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    driver = webdriver.Chrome(service=Service(), options=option)

    driver.get("https://www.rappad.co/insult-generator")

    driver.find_element(By.XPATH, f"//button[text()='Generate Insult']").click()
    insult = ""

    while insult == "":
        insult = driver.find_element(By.XPATH, f"//h1[@id='insult']").text

    return f"{name.upper()}, {insult}"

if __name__ == "__main__":
    print(insult("Rick Astley"))