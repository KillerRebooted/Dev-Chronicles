#'lst' is a list of length 'num-1'

def find_missing_no(num, lst):

    #Sum of 'n' Natural Numbers - Sum of given list

    return num*(num+1)//2 - sum(lst)

print(find_missing_no(5, [1, 4, 5, 2]))
print(find_missing_no(6, [4, 2, 3, 1, 5]))
