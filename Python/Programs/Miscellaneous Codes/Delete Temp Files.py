import os
    
Temp = r"C:\Users\rashm\AppData\Local\Temp"

for File in os.listdir(Temp):

    try:
        
        os.remove(os.path.join(Temp, File))
        print(f"{File} Deleted")

    except:

        print(f"Access to {File} is Denied")