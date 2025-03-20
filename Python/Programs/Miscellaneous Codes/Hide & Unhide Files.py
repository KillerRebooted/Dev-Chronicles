import os

current_loc = __file__.removesuffix(os.path.basename(__file__))

hidden_files = []

try:
    with open(f"{current_loc}Save File.txt", "r") as f:
        hidden_files = [i.removesuffix("\n") for i in f.readlines()]

except:
    pass

if os.path.exists(f"{current_loc}Save File.txt"):

    for i in hidden_files:
        os.popen(f'attrib +h "{i}"')

    os.remove(f"{current_loc}Save File.txt")


else:
    
    for i in os.listdir(current_loc):
    
        path = f"{current_loc}{i}"

        attributes = os.popen(f'attrib "{path}"').read().split()
    
        if "H" in attributes[1]:
            hidden_files.append(path)

    for i in hidden_files:
        os.popen(f'attrib -h "{i}"')

    with open(f"{current_loc}Save File.txt", "w+") as f:
        for i in hidden_files:
            f.write(f"{i}\n")