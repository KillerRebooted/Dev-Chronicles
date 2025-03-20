def Simplify_Moves(list, check_for, replace):

    count = 0
    list1 = []

    for i in range(len(list)):

        if i < count:

            continue

        if list[i : i+len(check_for)] == check_for:

            for j in replace:    
                
                list1.append(j)

            count = i + len(check_for)

        else:

            list1.append(list[i])

    return list1

list = ["U", "U", "y", "U", "y", "R", "R'"]

list = Simplify_Moves(list, ["U", "y", "U", "y"], ["U2", "y2"])
list = Simplify_Moves(list, ["R", "R'"], [])

for i in list:

    print(i, end=" ")