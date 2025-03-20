import os

File = input("Enter the Tasks name: ")

os.system(f"TASKKILL /F /IM {File}")