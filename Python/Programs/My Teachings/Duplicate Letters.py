def guess(word,secondword):

    lst1=[]
    lst2=[]
    evaluation=["x","x","x","x","x"]
    for letter in word:
        lst1.append(letter)
    for letter in secondword:
        lst2.append(letter)
    c_let= [i for i in lst1 if i in lst2]

    for pos, letter in enumerate(lst2):

        if letter in c_let:

            evaluation[pos] = letter

    print(evaluation)

     
guess("fubar","freak") #w.r.t. to Second Word
