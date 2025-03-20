current_year = 1600

if current_year % 4 == 0:
    february = 29

else:
    february = 28

if current_year % 100 == 0 and current_year % 400 == 0:
    february = 29

elif current_year % 100 == 0 and current_year % 400 != 0:
    february = 28

print(february)