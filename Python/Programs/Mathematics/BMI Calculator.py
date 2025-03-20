Weight = float(input("Enter your Weight in Kilograms: "))
Height = float(input("Enter your Height in Metres: "))

BMI = Weight/(Height*Height)

if BMI <= 18.5: health = "are Underweight"
elif 18.5 < BMI <= 25: health = "have a Healthy Weight"
elif 25 < BMI <= 30: health = "are Overweight"
else: health = "are Obese"

print(f"\nYour BMI is {BMI:.2f} and you {health}")
