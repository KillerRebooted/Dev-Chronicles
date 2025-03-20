print()

from datetime import datetime
from time import sleep

a = datetime(2007, 2, 2)
b = datetime(2021, 4, 29)
c = b - a

d = datetime.now()

e = d.strftime("%S")

f = c.days * 24 * 60 * 60 + int(e)

a = True

while a == True:
    print(f, end="\r")
    sleep(1)
    f = f + 1