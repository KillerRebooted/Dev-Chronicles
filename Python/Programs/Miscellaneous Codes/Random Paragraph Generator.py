import random, enchant

d = enchant.Dict("en_INDIA")

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets += alphabets.lower()

def rand_para_gen(para, words):
    for i in range(para):
        for j in range(words):

            suggestions = []

            while not suggestions:

                random_word = "".join(random.choices(alphabets, k=random.randint(2, 14)))
                suggestions = d.suggest(random_word)

                if suggestions and suggestions[0].isalpha() and len(suggestions[0]) > 1:
                    pass
                else:
                    suggestions = []

            print(suggestions[0], end=" ", flush=True)
        
        print()

rand_para_gen(8, 20)