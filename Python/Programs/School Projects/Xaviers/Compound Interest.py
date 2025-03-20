P = float(input("Enter the Principal Amount: "))
R = float(input("Enter the Rate of Interest: "))
T = float(input("Enter the Time Period in Years: "))
N = float(input("Enter 1 if Interest Compounded Annually, 2 for Half Yearly and 4 for Quarterly: "))

print()

n = N
N *= T

r = R
R /= 100

A = P*(1+(R/N))**(N*T)
CI = A-P

print(f"Compound Interest for ₹{P} for {r}% Interest for {T} Years compounded {n} Time(s) Annually is ₹{CI}")