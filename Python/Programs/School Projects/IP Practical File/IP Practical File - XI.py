#Program 1
print("\n"*5)

marks = [float(i) for i in input("Enter Marks separated by commas: ").split(",")]

print(f"Average Marks are: {sum(marks)/len(marks)}")

avg = sum(marks) / len(marks)

print("Grade ", end="")

if avg >= 90: print("A")
elif avg >= 75: print("B")
elif avg >= 40: print("C")
else: print("F")

#Program 2
print("\n"*5)

cost = float(input("Enter Cost: "))
discount = float(input("Enter Discount (in %): "))

print(f"Sale Price: {cost-(discount/100)*cost}")

#Program 3
print("\n"*5)

shape = input("Shape: ")

if shape == "triangle":
    side = float(input("Side: "))
    print(f"Perimeter: {3*side}, Area: {3**(1/2)/4 * side**2}")

elif shape == "circle":
    radius = float(input("Radius: "))
    print(f"Circumference: {2*3.14*radius}, Area: {3.14*radius**2}")

elif (shape == "rectangle") or (shape == "square"):
    l = float(input("Length: "))
    b = float(input("Breadth: "))
    print(f"Perimeter: {2*(l+b)}, Area: {l*b}")

#Program 4
print("\n"*5)

p = float(input("Principal: "))
r = float(input("Rate (in %): "))
t = float(input("Time Period (years): "))

print(f"Simple Interest: {p*r*t/100}, Compound Interest: {p*(1+r/100)**t - p : .2f}")

#Program 5
print("\n"*5)

cp = float(input("Cost Price: "))
sp = float(input("Sell Price: "))

print(f"Profit: Rs. {sp-cp}" if sp>cp else f"Loss: Rs. {cp-sp}")

#Program 6
print("\n"*5)

p = float(input("Principal: "))
r = float(input("Rate (in %): "))
t = float(input("Time Period (years): "))

rate = r/12/100
months = t*12

emi = p*(rate)*((1+(rate))**(months))/(((1+(rate))**(months))-1)

print(f"EMI: Rs.{round(emi)} p.m., Interest Payable: Rs.{round(emi*months)-p}, Total Payment: Rs.{round(emi*months)} (principal+interest)")

#Program 7
print("\n"*5)

a = float(input("Enter Amount: "))
g = float(input("Enter GST Rate (in %): "))

print(f"Your Total is Rs.{a + g/100*a} including GST (for {g}% GST rate)")

#Program 8
print("\n"*5)

l = [float(i) for i in input("Enter a List separated by commas: ").split(",")]

print(f"Min: {min(l)}, Max: {max(l)}")

#Program 9
print("\n"*5)

l = [float(i) for i in input("Enter a List separated by commas (Minimum 3 Elements): ").split(",")]

print(f"3rd Min: {(sorted(l))[2]}, 3rd Max: {(sorted(l))[-3]}")

#Program 10
print("\n"*5)

squares = [i*i for i in range(1, 101)]

print(f"Sum of First 100 Squares: {sum(squares)}")

#Program 11
print("\n"*5)

num = int(input("Enter a Number: "))
mul = int(input("Enter Number of Multiples: "))

multiples = []
for i in range(1, num+1):
    if num%i == 0:
        multiples.append(i)

print(f"The first {mul} Multiples of {num} are {multiples[:mul]}")

#Program 12
print("\n"*5)

string = input("Enter a String: ")

vowels = [i for i in string if i in "aeiouAEIOU"]

print(f"There are {len(vowels)} vowels in {string}")

#Program 13
print("\n"*5)

s = input("Enter a String: ")
l = input("Enter a Letter: ")

print(f"\nThe words starting with '{l}' are:", end=" ")
for i in s.split():
    if i[0] == l:
        print(i, end=" ")

#Program 14
print("\n"*5)

s = input("Enter a String: ")
l = input("Enter a Letter: ")

print(f"There are {s.count(l)} letter {l}(s) in {s}")

#Program 15
print("\n"*5)

country_capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover', 'India':'New Delhi'}

print(country_capitals)

#Program 16
print("\n"*5)
from random import randint as r

def ran(): return r(1, 100)

names = ["Chintu", "Shreyas", "Shresht", "Anchit", "Swasti", "Angel"]

d = {}
for i in range(len(names)):
    d[names[i]] = {"English": ran(), "Hindi": ran(), "Math": ran(), "Science": ran(), "SST": ran()}

print(d)

#Program 17
print("\n"*5)

d = {"Num 1": 1, "Num 2": 2, "Num 3": 3, "Num 4": 4, "Num 5": 5}

print(f"Minimum Value in Dictionary: {min(d.values())}")

#Program Zero
print("\n"*5)

ti = float(input("What's your annual income? "))

def calc(amount, percent):
    return (amount * percent) / 100

if ti <= 250000: tax = 0
elif ti <= 500000: tax = calc(ti - 250000, 5)
elif ti <= 750000: tax = calc(ti - 500000, 10) + 12500
elif ti <= 1000000:	tax = calc(ti - 750000, 15) + 37500
elif ti <= 1250000:	tax = calc(ti - 1000000, 20) + 75000
elif ti <= 1500000:	tax = calc(ti - 1250000, 25) + 125000
else: tax = calc(ti - 1500000, 30) + 187500

print(f"Total tax applicable at ₹{ti} is ₹{tax}")