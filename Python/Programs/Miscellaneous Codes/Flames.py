import subprocess
from time import sleep

# Cut Common Letters from both Names, only the first occurrences. Count the number of uncommon letters and count the number of letters starting from F wrapping around the word. Cut the letter that we end up on and continue the same count from the next letter until one letter remains. The last remaining letter determines your Relationship 😉

clear = lambda: subprocess.run("cls", shell=True)

#clear()

def intersection(a, b):
    uncommon = [[], []]
    b_copy = b.copy()
    for i in a:
        if i not in b_copy:
            uncommon[0].append(i)
        else:
            uncommon[0].append("")
            b_copy[b_copy.index(i)] = ""

    uncommon[1] = b_copy

    return uncommon

def to_fullwidth(lst):
    return [chr(ord(c) + 0xFEE0) if c != " " else c for c in lst]

flames_dict = {"F":"Friends", "L":"Love", "A":"Affection", "M":"Marriage", "E":"Enemy", "S":"Siblings"}
flames = to_fullwidth(list(flames_dict.keys()))

n1 = list(input("Enter First Name: ").upper().replace(" ", "").strip())
n2 = list(input("Enter Second Name: ").upper().replace(" ", "").strip())

n1 = to_fullwidth(n1)
n2 = to_fullwidth(n2)

n1_uncommon, n2_uncommon = intersection(n1, n2)

#clear()

print()
print(" ".join([" "] + n1))
print(" ".join([" "] + n2))

sleep(1)

iter = len([i for i in n1_uncommon if i == ""])
for i in range(iter):

    flame1 = n1_uncommon.index("")
    flame2 = n2_uncommon.index("")

    n1_uncommon[flame1] = "🔥"
    n2_uncommon[flame2] = "🔥"

    print("\033[2F", end="")
    print(" ".join([" "] + n1_uncommon[:flame1+1]), " ".join(n1[flame1+1:]))
    print(" ".join([" "] + n2_uncommon[:flame2+1]), " ".join(n2[flame2+1:]))

    sleep(1)

iter = max(len(n1), len(n2))
count = 0
for i in range(iter):

    if n1_uncommon[i:i+1] not in (["🔥"], []):
        count += 1
        n1_uncommon[i] = to_fullwidth([str(count)])[0] if count < 10 else str(count)
        sleep(0.5)

    print("\033[2F", end="")
    print(" ".join([" "] + n1_uncommon))
    print(" ".join([" "] + n2_uncommon))
    
    if n2_uncommon[i:i+1] not in (["🔥"], []):
        count += 1
        n2_uncommon[i] = to_fullwidth([str(count)])[0] if count < 10 else str(count)
        sleep(0.5)

    print("\033[2F", end="")
    print(" ".join([" "] + n1_uncommon))
    print(" ".join([" "] + n2_uncommon))

sleep(2)

print("\033[2F\033[K", end="")
print(" ".join(flames))

"""idx = 0
for _ in range(5):
    idx += count
    flames.pop(list(flames.keys())[idx%len(flames)-1])
    idx = idx%(len(flames)+1)-1

    if idx == -1:
        idx = len(flames)-1

print(*flames.values())"""