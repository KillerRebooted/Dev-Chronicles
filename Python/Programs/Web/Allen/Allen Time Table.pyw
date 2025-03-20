import os
import pandas as pd

clear = lambda: os.system("cls")

clear()

try:
    from selenium import webdriver

    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import Select

except:
    
    os.system("pip install selenium")
    os.system("pip install webdriver-manager")

    from selenium import webdriver

    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(), options=chrome_options)

driver.get("https://jaipur.allen.ac.in/time-table")

driver.maximize_window()


select = Select(driver.find_element(By.ID, 'SessionID'))
select.select_by_visible_text("2024-2025")

while True:
    try:
        select = Select(driver.find_element(By.ID, 'DivisionID'))
        select.select_by_visible_text("JEE DIVISION")
        break
    except:
        pass

while True:
    try:
        select = Select(driver.find_element(By.ID, 'BatchID'))
        select.select_by_visible_text("5J2-D1C")
        break
    except:
        pass

time_table = []
while time_table == []:
    time_table = [table for table in driver.find_elements(By.TAG_NAME, "table")]

df = {"Date":[''], "Day":[''], "Class Type":[''], "Class Time":[''], "Subject":['']}
for table in time_table:

    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows[1:]:
        elements = row.find_elements(By.TAG_NAME, "td")

        for idx, column in enumerate(df):
            df[column].append(elements[idx].text)

    for idx, column in enumerate(df):
        df[column].append("")

time_table = pd.DataFrame(df).to_string(index=False)

driver.close()

os.system("cls")

with open(f"{os.path.dirname(os.path.abspath(__file__))}/Allen Time Table.txt", "r") as f:
    content = "".join(f.readlines())

if content != time_table:
    
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/Allen Time Table.txt", "w+") as f:
        f.write(time_table)