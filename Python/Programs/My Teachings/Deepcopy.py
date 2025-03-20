#Deepcopy and Copy are different

from random import randint
import copy

def createRoute():
    route = []
    for horizon in range(8):
        row = []
        for vertical in range(4):
            row.append(randint(0, 50))
        route.append(row)
    return route

def printRoute(list):
    for i in range(8):
        for j in range(4):
            print("%3d" % list[i][j], end=" ")
    print()

def main():
    route = createRoute()
    copyRoute = copy.deepcopy(route)
    route[0][0] = 250
    printRoute(route)
    printRoute(copyRoute)

main()
