import PyPDF2

loc = f"C:\\Users\\Shreyas Nair\\Desktop\\Important Documents"
    
# creating a pdf file object 
pdfFileObj = open(f'{loc}/Attempt 1.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfReader(pdfFileObj) 

def grab(word):
    qids = []
    for page in pdfReader.pages:
        
        text = page.extract_text()

        for idx, i in enumerate(text):
            if text[idx:idx+len(word)] == word:
                q_idx = idx

                colon_idx = q_idx + text[q_idx:q_idx+15].index(":")

                if word == "Chosen Option":
                    add = 1
                elif "Option" in word:
                    add = 10
                elif len(qids) < 25:
                    add = 9
                else:
                    add = 10

                qid = text[colon_idx+2:colon_idx+2+add]

                if qid == "736475101 ":
                    qid = "7364751011"

                qids.append(qid)

    if word == "Question ID":
        scratch_list = list(range(21,26)) + list(range(46,51)) + list(range(71,76))
        qids = [i for idx, i in enumerate(qids, start=1) if idx not in scratch_list]

    return qids

question_set = dict(zip (grab("Question ID"), (list(zip(grab("Option 1"), grab("Option 2"), grab("Option 3"), grab("Option 4"))))))
option_chosen = grab("Chosen Option")

final_key = {}
for q, a in question_set.items():

    chosen = option_chosen[list(question_set.keys()).index(q)]

    final_key[q] = chosen if chosen == "-" else a[int(chosen)-1]

# closing the pdf file object 
pdfFileObj.close()


pdfFileObj = open(f'{loc}/Question Attempt 1.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfReader(pdfFileObj) 

words = ("Section A", "Section\nA")

q_no = 1

check_key = {}
for page in pdfReader.pages:

    text = page.extract_text()

    for idx, i in enumerate(text):
        if (text[idx:idx+len(words[0])] == words[0]) or (text[idx:idx+len(words[1])] == words[1]):
            q_idx = idx

            if (text[idx:idx+len(words[0])] == words[0]):
                id = text[q_idx+len(words[0]):q_idx+len(words[0])+21]
            elif (text[idx:idx+len(words[1])] == words[1]):
                id = text[q_idx+len(words[1]):q_idx+len(words[1])+21]

            if q_no < 21:
                check_key[id[:9]] = id[9:19].replace("\n", "")
            else:
                check_key[id[:10]] = id[10:20].replace("\n", "")

            q_no += 1

# closing the pdf file object 
pdfFileObj.close()

correct = 0
wrong = 0
unnattempted = 0

marks = 0
for qid, aid in final_key.items():

    if ((check_key[qid] == aid)) and aid != "-":
        marks += 4
        delta = 4
        correct += 1
    elif aid == "-":
        marks += 0
        delta = 0
        unnattempted += 1
    else:
        marks -= 1
        delta = -1
        wrong += 1

    print(f"{qid}: {aid}, {check_key[qid]}", delta)

print()
print(f"You Scored {marks} Marks in MCQs:\n\n{correct} Correct\n{wrong} Wrong\n{unnattempted} Unattempted")