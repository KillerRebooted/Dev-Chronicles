list = [14, 13, 2, 12] #As close to a Square as possible

def getSquare(list):
    
    for i in range(1, max(list)+1):

        output = []
        num = 0

        for j in list:

            output.append([i]*(j//i))

            num += j//i

            if j%i != 0:

                output[-1].append(j%i)

                num += 1

        if num == i:

            return output

    i = int( sum(list) ** (1/2) // 1)

    output = []
    
    for j in list:

        output.append([i]*(j//i))

        num += j//i

        if j%i != 0:

            output[-1].append(j%i)

            num += 1

    return output

for i in getSquare(list):

    for j in i:

        print("* "*j)
