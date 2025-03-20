birth_year = int(input("Enter the year of your birth: "))
current_year = int(input("Enter the current year: "))
birth_month = int(input("Enter your birth month(1-12): "))
current_month = int(input("Enter the current month(1-12): "))
birth_date = int(input("Enter your birth date(1-31): "))
current_date = int(input("Enter the current date(1-31): "))
months = 12

#If data entered is wrong

#if (birth_month > 12) or (current_month > 12) or (birth_date > 31) or (current_date > 31) or (current_date < 1) or (birth_date < 1) or (birth_month < 1) or (current_month < 1) or (current_year > 10000) or (birth_year < 1000):
 #   print ("The data entered is wrong")

#For February if wrong date

#if (current_month == 2) and (current_date > 29) or (birth_date > 29):
 #   print ("Invalid date")

#If the birth year is a leap year

if (birth_year % 4 == 0) and (birth_month == 2) and (current_month < birth_month):
    print (f"You are {current_year - birth_year} years old and there are {birth_month - current_month} month(s) left and for your birthday")
elif (birth_year % 4 == 0) and (birth_month == 2) and (current_month > birth_month):
    print (f"You are {current_year - birth_year} years old and there are {(months - current_month) + birth_month} month(s) left for your birthday")

#If date is 29 or greater in feb on an ordinary year

#if (birth_year % 4 != 0) and (birth_year % 400 != 0) and (birth_date >= 29):
 #   print (f"February dosen't have this many days in {current_year}")

#The leap year thinggy

if current_year % 4 == 0:
    february = 29
else:
    february = 28

#THE special condition

if (current_year % 100 == 0) and (current_year % 400 == 0):
    february = 29
elif (current_year % 100 == 0) and (current_year % 400 != 0):
    february = 28

#If dates are wrong

#if (birth_month == 4) and (birth_date > 30) or (current_date > 30):
   # print ("there are only 30 days in April")

#if (birth_month == 6) and (birth_date > 30) or (current_date > 30):
    #print ("There are only 30 days in June")

#if (birth_month == 9) and (birth_date > 30) or (current_date > 30):
 #   print ("There are only 30 days in September")
    
#if (birth_month == 11) and (birth_date > 30) or (current_date > 30):
 #   print ("There are only 30 days in November")

#THE MONTHS

#january = 31
#march = 31
#april = 30
#may = 31
#june = 30
#july = 31
#august = 31
#september = 30
#october = 31
#november = 30
#december = 31
    
#Giving answers

if (current_month < birth_month) and (birth_date < current_date):
    print(f"You are {current_year - birth_year - 1} years old and there are {birth_month - current_month} month(s) left and for your birthday")
elif (current_month > birth_month) and (current_date > birth_date): 
    print(f"You are {current_year - birth_year} years old and there are {(months - current_month) + birth_month} month(s) left and for your birthday")
elif (current_month < birth_month) and (current_date > birth_date):
    print(f"You are {current_year - birth_year} years old and there are {(months - current_month) + birth_month} month(s) left and for your birthday")