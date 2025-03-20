from os import system

clear = lambda: system('cls')

clear()

Range = input("Enter 2 Numbers separated by commas (34, 44): ").split(',')

if len(Range) < 2:

	print("\nError\n")

temp_list = []

for i in Range:

	try:

		temp_list.append(int(i))

	except:

		print("\nError\n")
		quit()

Range = temp_list

divisibility = input("Enter the Number you want its Divisibility with: ")

try:

	divisibility = int(divisibility)

except:

	print("\nError\n")
	quit()

if min(Range)%divisibility == 0:

	start = min(Range)

else:

	start = min(Range) + (divisibility - min(Range)%divisibility)

end = max(Range) - max(Range)%divisibility

print()

for i in range(start, end+1, divisibility):

	if i == end:

		print(i)

		break

	print(f"{i}, ", end="")


print()

print(f"\nThe Length of this AP is {len(range(start, end+1, divisibility))}")
print(f"The Sum of this AP is {sum(range(start, end+1, divisibility))}")