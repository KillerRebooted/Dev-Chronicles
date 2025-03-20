H = float(input("Enter your height in meters: "))
W = float(input("Enter your weight in kilograms: "))
BMI = W/(H*H)
print (BMI)
if BMI < 18.5:
    print("You are underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You have a healthy weight")
elif BMI > 24.9 and BMI <= 30:
    print("You are overweight")
else:
    print ("You are Obese")
