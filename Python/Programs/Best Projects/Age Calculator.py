from os import system
from time import sleep
from datetime import datetime

clear = lambda: system("cls")

clear()

print(r"Please NOTE: This Program is not 100% accurate as it is made by a 9th Grader, but you won't sit and find my Errors so.....")
print()
input("Press ENTER to continue....")

clear()

print()
print ('Type in Proper Format as Instructed')
print()
print ('Aap Khel Rahe Hai Kaun Banega Crorepati aur yeh rah pehla Sawal Aapki Computer Screen par:')

sleep(2)

print()

birth_date = int(input("What is the Date on which you were Born (1-31): "))
print()
birth_month = int(input("What is the Month in which you were Born (from 1-12): "))
print()
birth_year = int(input("What is the Year in which you were Born (2007, 2011 etc.): "))
print()
birth_time = (input("""Enter the Time of your Birth in 24-Hour Format:-

0555 means  5:55 AM (Early Morning)
1755 means  5:55 PM (Evening)
0055 means 12:55 AM (Midnight)
1255 means 12:55 PM (Noon)

or Enter 0000 if you don't know/remember your Birth Time. It would be Funny if your Birth Time is 0000 :)

- """))

#If 29 is Entered as a Date during an Ordinary Year

if (birth_year % 4 != 0) and (birth_month == 2) and (birth_date == 29):
    print()
    print(f"There are only 28 Days in February in {birth_year}")
    print()
    exit()

#If Year is Divisible by 400 as Years like 1900 are not Leap Years unlike 2000

if (birth_year % 100 == 0) and (birth_year % 400 != 0) and (birth_date >= 29) and (birth_month == 2):
    print()
    print(f"{birth_year} is not a Leap Year")
    print()
    exit()

#If February has more than 28 Days

if (birth_month == 2) and ((birth_date == 30) or (birth_date == 31)):
    print()
    print("February doesn't have this many Days")
    print()
    exit()

#If Birth Year is not 4-Digit

if birth_year < 1000:
    print()
    print("Year should be between 1000 and 9999 years")
    print()
    exit()

if birth_year > 9999:
    print()
    print("Year should be between 1000 and 9999 years")
    print()
    exit()

#If Dates are Invalid

if birth_month < 1:
    print()
    print("Month should be between 1-12")
    print()
    exit()

if birth_month > 12:
    print()
    print("Month should be between 1-12")
    print()
    exit()

if birth_date < 1:
    print()
    print("Date should be 1 or Greater")
    print()
    exit()

if birth_date > 31:
    print()
    print("Date should be 31 or Lesser")
    print()
    exit()

if (birth_month == 4) and (birth_date == 31):
    print()
    print("There are only 30 Days in April")
    print()
    exit()

if (birth_month == 6) and (birth_date == 31):
    print()
    print("There are only 30 Days in June")
    print()
    exit()

if (birth_month == 9) and (birth_date == 31):
    print()
    print("There are only 30 Days in September")
    print()
    exit()

if (birth_month == 11) and (birth_date == 31):
    print()
    print("There are only 30 Days in November")
    print()
    exit()

print()
print()

current_date = int(input("What is the Date Today (1-31): "))
print()
current_month = int(input("What is the Month Currently (from 1-12): "))
print()
current_year = int(input("What is the Year Currently: "))

clear()

#If 29 is Entered as a Date during an Ordinary Year

if (current_year % 4 != 0) and (current_month == 2) and (current_date == 29):
    print()
    print(f"There are only 28 Days in February in {current_year}")
    print()
    exit()

#If Year is Divisible by 400 as Years like 1900 are not Leap Years unlike 2000

if (current_year % 100 == 0) and (current_year % 400 != 0) and (current_date >= 29) and (birth_month == 2):
    print()
    print(f"{current_year} is not a Leap Year")
    print()
    exit()    

#If February has more than 28 Days

if (current_month == 2) and ((current_date == 30) or (current_date == 31)):
    print()
    print("February doesn't have this many Days")
    print()
    exit()

#If Birth Year is not 4-Digit

if current_year < 1000:
    print()
    print("Year should be between 1000 and 9999 years")
    print()
    exit()

if current_year > 9999:
    print()
    print("Year should be between 1000 and 9999 years")
    print()
    exit()

#If Dates are Invalid

if (current_month == 4) and (current_date == 31):
    print()
    print("There are only 30 Days in April")
    print()
    exit()

if current_month == 6 and current_date == 31:
    print()
    print("There are only 30 Days in June")
    print()
    exit()

if current_month == 9 and current_date == 31:
    print()
    print("There are only 30 Days in September")
    print()
    exit()

if current_month == 11 and current_date == 31:
    print()
    print("There are only 30 Days in November")
    print()
    exit()

if current_month < 1:
    print()
    print("Month should be between 1-12")
    print()
    exit()

if current_month > 12:
    print()
    print("Month should be between 1-12")
    print()
    exit()

if current_date < 1:
    print()
    print("Date should be 1 or Greater")
    print()
    exit()

if current_date > 31:
    print()
    print("Date should be 31 or Lesser")
    print()
    exit()

#If Birth Year is Greater than Current Year

if birth_year > current_year:
    print()
    print("How can your Birth Year be Greater than the Current Year?")
    print()
    exit()

#Assigning Months their respective Number of Days

january = 31

#Assigns Value to February according to the Type of Year

if current_year % 4 == 0:
    february = 29

else:
    february = 28

#Special Condiion if the Year is Divisible by 100

if current_year % 100 == 0 and current_year % 400 == 0:
    february = 29

elif current_year % 100 == 0 and current_year % 400 != 0:
    february = 28

march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31

Months = {1: january, 2: february, 3: march, 4: april, 5: may, 6: june, 7: july, 8: august, 9: september, 10: october, 11: november, 12: december}

age_year = current_year - birth_year

if current_month < birth_month:
    age_year = age_year - 1

if (current_month == birth_month) and (current_date < birth_date):
    age_year -= 1

if birth_date < current_date:
    age_date = current_date - birth_date
elif birth_month == 1:
    age_date = january - birth_date + current_date
elif birth_month == 2:
    age_date = february - birth_date + current_date
elif birth_month == 3:
    age_date = march - birth_date + current_date
elif birth_month == 4:
    age_date = april - birth_date + current_date
elif birth_month == 5:
    age_date = may - birth_date + current_date
elif birth_month == 6:
    age_date = june - birth_date + current_date
elif birth_month == 7:
    age_date = july - birth_date + current_date
elif birth_month == 8:
    age_date = august - birth_date + current_date
elif birth_month == 9:
    age_date = september - birth_date + current_date
elif birth_month == 10:
    age_date = october - birth_date + current_date
elif birth_month == 11:
    age_date = november - birth_date + current_date
elif birth_month == 12:
    age_date = december - birth_date + current_date

if current_date < birth_date and current_month == birth_month:
    age_date = birth_date - current_date

if current_month < birth_month and current_date > birth_date:
    age_month = birth_month - current_month
    age_month = 12 - age_month

if current_month < birth_month and current_date < birth_date:
    age_month = birth_month - current_month
    age_month = 12 - age_month - 1

if current_month > birth_month and current_date > birth_date:
    age_month = current_month - birth_month

if current_month > birth_month and current_date < birth_date:
    age_month = current_month - birth_month - 1

if current_month > birth_month and current_date == birth_date:
    age_month = current_month - birth_month

if current_month < birth_month and current_date == birth_date:
    age_month = 12 + (current_month - birth_month)

if current_year == birth_year:
    age_year = 0

if current_month == birth_month:
    age_month = 0

if (current_month == birth_month) and (current_date < birth_date):
    age_month = 11
    age_date = 31 - (birth_date - current_date)

if current_date == birth_date:
    age_date = 0

birth_hour = int(birth_time[:2])
birth_minute = int(birth_time[2:])

c_date = datetime.now()

current_hour = int(c_date.strftime("%H"))
current_minute = int(c_date.strftime("%M"))

hour = int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).days*24) + int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).seconds//3600)

minute = int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).days*24*60) + int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).seconds//60)

seconds = int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).days*24*60*60) + int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).seconds)

milleseconds = int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).days*24*60*60*100) + int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).microseconds//10000) + int(c_date.strftime("%f"))//10000

microseconds = int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).days*24*60*60*1000000) + int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).microseconds) + int(c_date.strftime("%f"))

age_days = int((datetime(current_year, current_month, current_date, current_hour, current_minute) - datetime(birth_year, birth_month, birth_date, birth_hour, birth_minute)).days)

print(f"Your Age is {age_year} Year(s), {age_month} Month(s) and {age_date} Day(s)")
print()
print(f"or {age_year * 12 + age_month} Month(s) and {age_date} Day(s)")
print()

print(f"or {age_days // 7} Week(s) and {age_days % 7} Day(s)")

print()
print(f"or {age_days} Day(s)")
print()

print(f"or {hour} Hours")
print()

print(f"or {minute} Minutes")
print()

print(f"or {seconds} Seconds")
print()

print(f"or {milleseconds} Milleseconds")
print()

print(f"or {microseconds} Microseconds")
print()

day = datetime(birth_year, birth_month, birth_date)
day = day.strftime("%A")

print(f"You were Born on a {day}")
print()

#It Would've been too much effort if I made it as detailed as the Age. Therefore, it only Specifies a generalised Time Left

if (birth_month > current_month):
    
    month_left = birth_month-current_month
    Text = " Month(s) left for your next Birthday"

elif (current_month > birth_month):
    
    month_left = 12 + (birth_month-current_month)
    Text = " Month(s) left for your next Birthday"

elif (birth_month == current_month) and (birth_date == current_date):
    
    month_left = ""
    Text = "TODAY IS YOUR BIRTHDAY!"

elif (birth_month == current_month) and (birth_date < current_date):
    
    month_left = current_date-birth_date
    Text = " Day(s) ago, you Celebrated your Birthday and your next Birthday is in 11 Months"

elif (birth_month == current_month) and (birth_date > current_date):
    
    month_left = birth_date - current_date
    Text = " Day(s) left for your Birthday!"

if current_date > birth_date:
    
    month_left -= 1

if month_left == 0:

    month_left = Months[current_month] - age_date
    Text = " Day(s) left for your Birthday!"

print(str(month_left) + Text)
print()
