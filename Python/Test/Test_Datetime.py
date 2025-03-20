from datetime import date
b_date = date(2021, 4, 23)
c_date = date(2021, 4, 24)
age = c_date - b_date
print(age.days)

from datetime import datetime
b_date = datetime(2007, 2, 4, 17, 55, 46)
c_date = datetime.today()
age = c_date - b_date
print(age)

now = datetime.now()
age = now.strftime("%m")
print(int(age))