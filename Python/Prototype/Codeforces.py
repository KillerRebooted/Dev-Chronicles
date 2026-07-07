t = int(input())

for i in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    swaps = 0

    for idx in range(n):
        if start[idx] > end[idx]:
            if idx != n-1:        
                for j in range(idx+1, n):
                    if start[j] <= end[idx]:
                        element = start[j]
                        start.pop(j)
                        start.insert(idx, element)
                        swaps += j - idx
                        break
                else:
                    print(-1)
                    break
            else:
                print(-1)
                break

    else:
        
        print(swaps)