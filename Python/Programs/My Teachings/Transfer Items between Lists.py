list1 = [['[x]homework', '[x]eat','stretch'], ['[x]final', 'school'], ['sleep','midterm']]
new_list = [list() for i in range(len(list1))]
new_list[2] = list1[2]

items = 0
for i in range(len(list1)-1):
    for j in list1[i]:
        if "[x]" in j:
            new_list[2].append(j.replace("[x]", ""))
            items += 1
        else:
            new_list[i].append(j)

print(list1, new_list, items)
