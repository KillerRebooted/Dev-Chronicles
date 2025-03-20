import os

File = f"{__file__.removesuffix(os.path.basename(__file__))}Hidden.txt"
os.popen(f'attrib +h "{File}"')

print(f'attrib "{File}"')

attributes = os.popen(f'attrib "{File}"').read().split()

print()
for i in attributes:
    print(i)

print()
print("Hidden" if "H" in attributes[1] else "Not Hidden")