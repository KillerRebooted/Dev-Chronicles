import matplotlib.pyplot as plt
import os

with open(f"{__file__.removesuffix(os.path.basename(__file__))}Letter Frequency Test.txt", "r", encoding = "utf-8") as f:

	content = f.read()

alphabets = "abcdefghijklmnopqrstuvwxyz"
data = {}

for i in alphabets:
	
	count = content.count(i.lower()) + content.count(i.upper())

	if count != 0:

		data[i.upper()] = count

pie_data = dict(sorted(data.items(), key=lambda item: item[0], reverse = True))

x = pie_data.keys()
y = pie_data.values()

exp = [0 if i != max(y) else 0.07 for i in y]

plt.pie(y, labels = x, radius = 1.2, startangle=90, shadow = False, explode = exp)

legend_data = [f"{i[0]}: {i[1]}" for i in (sorted(data.items(), key=lambda item: item[1], reverse = True))]

plt.legend(
	legend_data, 
	title ="Letter Count",
	loc ="center right",
	bbox_to_anchor =(1, 0, 0.5, 1)
)

plt.title("Letter Frequency Table\n\n")

plt.show()
