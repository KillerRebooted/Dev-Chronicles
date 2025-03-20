import datetime

dt = datetime.datetime.now()

# dt = dt.replace(hour=17)

if dt.hour < 12:

    Wish = "Morning"

elif (dt.hour >= 12) and (dt.hour < 18):

    Wish = "Afternoon"

else:

    Wish = "Evening"

print(f"Good {Wish}")