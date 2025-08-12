# Cut Common Letters from both Names, only the first occurrences. Count the number of uncommon letters and count the number of letters starting from F wrapping around the word. Cut the letter that we end up on and continue the same count from the next letter until one letter remains. The last remaining letter determines your Relationship 😉

def intersection(a, b):
    for i in b.copy():
        try:
            a.remove(i)
            b.remove(i)
        except:
            pass

    return list(a+b)

n1 = list(input("Enter First Name: ").lower().strip())
n2 = list(input("Enter Second Name: ").lower().strip())

flames = {"F":"Friends", "L":"Love", "A":"Affection", "M":"Marriage", "E":"Enemy", "S":"Siblings"}

count = len(intersection(n1, n2))

idx = 0
for _ in range(5):
    idx += count
    flames.pop(list(flames.keys())[idx%len(flames)-1])
    idx = idx%(len(flames)+1)-1

    if idx < 0:
        idx = 0

print(*flames.values())