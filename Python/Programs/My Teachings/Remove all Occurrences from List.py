def spell(string):

    a = "aa"
    b = "bb"
    c = "ccc"
    lst = string.split() #['aa', 'bb', 'ccc', 'aa']

    lst = list(filter(lambda i: i != a, lst)) #Removes all occurrences of a
    lst = list(filter(lambda i: i != b, lst)) #Removes all occurrences of b
    lst = list(filter(lambda i: i != c, lst)) #Removes all occurrences of c

    if len(lst)>1:
        return "NO"
    else:
        return "YES"
print(spell("aa ccc bb aa"))
