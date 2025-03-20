from time import sleep

#Letter by Letter

def LbL(Sentence, Time):

    for i in Sentence:
        
        print(i, end = "", flush=True)
        sleep(Time)

    return ""

LbL("Hi, this is a Sentence to Test the Code.", 0.1)