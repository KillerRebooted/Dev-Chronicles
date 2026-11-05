from time import sleep
import math

# Cut Common Letters from both Names, only the first occurrences. Count the number of uncommon letters and count the number of letters starting from F wrapping around the word. Cut the letter that we end up on and continue the same count from the next letter until one letter remains. The last remaining letter determines your Relationship 😉

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

def to_fullwidth(lst, reverse=False):
    if reverse:
        return [chr(ord(c) - 0xFEE0) if c != " " else c for c in lst]
    return [chr(ord(c) + 0xFEE0) if c != " " else c for c in lst]

flames_dict = {"F":"Friends 🫂", "L":"Love 💏", "A":"Affection 😚", "M":"Marriage 💍", "E":"Enemy 🔪", "S":"Siblings 👨‍👩‍👧‍👦"}
flames = to_fullwidth(list(flames_dict.keys()))

n1 = list(input("Enter First Name: ").upper().strip())
n2 = list(input("Enter Second Name: ").upper().strip())

og_n1 = "".join(n1).title()
og_n2 = "".join(n2).title()

n1 = to_fullwidth(list("".join(n1).replace(" ", "")))
n2 = to_fullwidth(list("".join(n2).replace(" ", "")))

n1_uncommon, n2_uncommon = intersection(n1, n2)

print()
print(" ".join([" "] + n1))
print(" ".join([" "] + n2))

sleep(1)

iter = len([i for i in n1_uncommon if i == ""])
for i in range(iter):

    flame1 = n1_uncommon.index("")
    flame2 = n2_uncommon.index("")

    n1_uncommon[flame1] = "\033[9m" + "\033[1m" + "\033[31m" + n1[flame1] + "\033[0m"
    n2_uncommon[flame2] = "\033[9m" + "\033[1m" + "\033[31m" + n2[flame2] + "\033[0m"

    print("\033[2F", end="")
    print(" ".join([" "] + n1_uncommon[:flame1+1]), " ".join(n1[flame1+1:]))
    print(" ".join([" "] + n2_uncommon[:flame2+1]), " ".join(n2[flame2+1:]))

    sleep(0.8)

iter = max(len(n1), len(n2))
count = 0
for i in range(iter):

    if n1_uncommon[i:i+1] and not n1_uncommon[i].endswith("\033[0m"):
        count += 1
        n1_uncommon[i] = "\033[1m" + to_fullwidth([str(count)])[0] if count < 10 else str(count)
        n1_uncommon[i] = "\033[1m" + n1_uncommon[i] + "\033[0m"
        sleep(0.35)

    print("\033[2F", end="")
    print(" ".join([" "] + n1_uncommon))
    print(" ".join([" "] + n2_uncommon))
    
    if n2_uncommon[i:i+1] and not n2_uncommon[i].endswith("\033[0m"):
        count += 1
        n2_uncommon[i] = to_fullwidth([str(count)])[0] if count < 10 else str(count)
        n2_uncommon[i] = "\033[1m" + n2_uncommon[i] + "\033[0m"
        sleep(0.35)

    print("\033[2F", end="")
    print(" ".join([" "] + n1_uncommon))
    print(" ".join([" "] + n2_uncommon))

sleep(2)

print("\033[F\033[K"*2, end="")
print(f"{og_n1} and {og_n2} have {count} uncommon letters\n")
print(" ".join(flames))
print(f"\033[1F", end="")

nums = [to_fullwidth([str(i)])[0] if i < 10 else str(i) for i in range(1, count+1)]
latest_flames_letter = None
for flame_count in range(5):
    for i in range(1, count+1):

        print("\033[1m" + " ".join(flames) + "\033[0m")

        skip = 0
        while latest_flames_letter and (flames[skip] != latest_flames_letter):
            print("  ", end=" ")
            skip += 1

        if skip == len(flames)-1:
            skip = 0
            latest_flames_letter = None
            print("\r\033[K", end="")

        rows = math.ceil((i + skip + 1)/(len(flames)-flame_count))
        count_to_print = 1
        for row in range(rows):
            for idx in range(skip, len(flames)):
                if not flames[idx].endswith("\033[0m"):
                    print(nums[count_to_print-1], end=" ")
                    count_to_print += 1
                    if count_to_print > i:
                        if count_to_print > count:
                            flames[idx] = "\033[9m" + "\033[38;2;255;165;0m" + flames[idx] + "\033[0m"
                            latest_flames_letter = flames[idx]
                        break
                else:
                    print("  ", end=" ")
            print()
            skip = 0
            if count_to_print > i:
                break

        print(f"\033[1F\033[K"*(row+2), end="")

        sleep(0.25)

print("\033[1m" + " ".join(flames) + "\033[0m")
print()

relationship = to_fullwidth([flame for flame in flames if not flame.endswith("\033[0m")][0], reverse=True)[0]

print(f"The Relationship between {og_n1} and {og_n2} is: {flames_dict[relationship]}")