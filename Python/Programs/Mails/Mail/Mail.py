import os, smtplib, webbrowser
from datetime import datetime
from time import sleep
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# @gmail.com only

clear = lambda: os.system("cls")

clear()
print()

Mail_Name = input("Save Mail with Name: ")
Mail_Name = Mail_Name + ".txt"

Password_Directory = f"{__file__.removesuffix(os.path.basename(__file__))}Saved Passwords"
Mail_Directory = f"{__file__.removesuffix(os.path.basename(__file__))}Mails\\{Mail_Name.removesuffix('.txt')}"
Mail_Location = f"{__file__.removesuffix(os.path.basename(__file__))}Mails\\{Mail_Name.removesuffix('.txt')}\\{Mail_Name}"

if not os.path.exists(Mail_Directory):

    if not os.path.exists(f"{__file__.removesuffix(os.path.basename(__file__))}Mails"):

        os.mkdir(f"{__file__.removesuffix(os.path.basename(__file__))}Mails")

    os.mkdir(Mail_Directory)

if not os.path.exists(Password_Directory):

    os.mkdir(Password_Directory)

print("\nType the Mail in The Notepad File that is about to Open and Press Ctrl+S when done and close the file")
print(f"Place any attchments you want to send in '{Mail_Directory}'")
print("The attachments shouldn't exceed 25MB in total.")
input("\nEnter to Continue...")

File = os.open(Mail_Location, os.O_CREAT)
os.close(File)

os.system(f'"{Mail_Location}"')

print()
input("Press Enter When Ready: ")

Mail = str(datetime.now())
Mail = Mail + """

"""

with open(Mail_Location, "r") as mail:
    
    for line in mail:
	    Mail += line

def E_Mail(Mail):
    
    clear()
    print(Mail)
    print()

    Correction = input("Is the Mail Correct? (y/n): ")

    while Correction == "n":
    
        File = os.open(Mail_Location, os.O_CREAT)
        os.close(File)
        os.system(f'"{Mail_Location}"')

        print()
        input("Press Enter When Ready: ")

        Mail = str(datetime.now())
        Mail = Mail + """

"""

        with open(Mail_Location, "r") as mail:
    
            for line in mail:
                Mail += line

        clear()
        print(Mail)
        print()

        Correction = input("Is the Mail Correct? (y/n): ")

E_Mail(Mail)

clear()

Sender_Mail = input("Enter Sender's Mail: ")
print()
Receiver_Mail = input("Enter Receiver's Mail (Multiple Recipients separated by commas): ").split(",")
Receiver_Mail = [i.strip() for i in Receiver_Mail]
print()
Subject = input("Subject of Mail: ")

File_Name = f"{Password_Directory}\\{Sender_Mail[:Sender_Mail.index('@')]}"

Have_Password = Path(File_Name + ".txt")

if Have_Password.exists():
    
    print()
    print("Password Found")

    with open(Have_Password, "r") as mail:
    
        for line in mail:
	        Password = line

else:
    
    print()
    print("Password Not Found")
    sleep(2)
    print()
    FA = input("Do You Have 2FA Enabled on Sender's Account (y/n): ")
    print()
    
    if FA == "y":
        
        print("You will be Redirected to Your Google Account to get Your App Password. Login to your Google Account")
        sleep(3)
        print("Click on 'Select App' and Select 'Mail'. Then 'Select Device' and 'Windows Computer' or 'Other (Custom Name)' and Copy the Generated Password")
        print()
        input("Press Enter when Ready: ")

        webbrowser.open("https://myaccount.google.com/apppasswords?rapt=AEjHL4Oqj4VaBl17Uv6Vq6ydNNe57S23koLmeLvUXR-iRgG2wqs_5EfvnyGnrXT8QCoIfM5aIX2ClPVLHzMErVSydOsAYk-RgQ")

        Password = input("\nEnter the App Password: ")

    else:

        print("You will be Redirected Your Google Account")
        sleep(3)
        print("Toggle the Setting On")
        print()
        input("Press Enter when Ready: ")

        webbrowser.open("https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4MrMNaz5m_UZl07TU_ql-j3tkwIF-i0zIK1TWQnPSWLVUkX3gwS2Cpww_M4m23Y9TxsQrz-qOFdutocjil1XcHHVNef7w")

        Password = input("\nEnter Your Mail Password: ")

    File = os.open(f"{File_Name}.txt", os.O_CREAT|os.O_WRONLY)

    os.write(File, Password.encode())
    os.close(File)


msg = MIMEMultipart()
msg["Subject"] = Subject
msg["From"] = Sender_Mail
msg["To"] = ", ".join(Receiver_Mail)

msg.attach(MIMEText(Mail))

for f in os.listdir(Mail_Directory):

    if f == Mail_Name:

        continue
    
    with open(f"{Mail_Directory}\\{f}", "rb") as file:

        file_loc = f"{Mail_Directory}\\{f}"
        
        attachment = MIMEApplication(
                
                file.read(),
                Name=os.path.basename(file_loc)
            
            )
        # After the file is closed
        
    attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_loc)}"'
    msg.attach(attachment)

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(Sender_Mail, Password)

server.sendmail(Sender_Mail, Receiver_Mail, msg.as_string())
server.quit()

print()
print("Mail Sent Successfully")
sleep(2)
print("Password Saved as " + Sender_Mail[:Sender_Mail.index('@')] + ".txt")
print()
print(f"If You want to Delete the Password, open '{Password_Directory}' and Delete it.")