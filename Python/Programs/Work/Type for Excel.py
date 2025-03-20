import pandas as pd
import pyautogui as pa
import time

df = pd.read_excel("Prototype\Book1.xlsx")

time.sleep(3)

for ind in df.index:
            
    pa.write(f"{df['BE Amount for year 2024-2025'][ind]}")
    pa.press("tab", presses=7)
