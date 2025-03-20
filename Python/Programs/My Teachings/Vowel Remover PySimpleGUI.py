import PySimpleGUI as sg

alphabet = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'10',
'k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17','r':'18','s':'19','t':'20',
'u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}

vowels = {'a','e','i','o','u'}

layout = [

[sg.Text('Word:', size=(15,1)), sg.Input(enable_events=True, key='WORD', size=(25,1))],
[sg.Text('Number:', size=(15,1)), sg.Input(key='NUMBER', size=(25,1))],
[sg.Text('Result:', size=(15,1)), sg.Input(key='RESULT', size=(25,1))],
]

window = sg.Window('MAIN',  layout, finalize=True,element_justification='c')


while True:

    event, values = window.read()
    #print(event, values)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    elif event == 'WORD':        
        
        string1 = values['WORD']
        string2 = '-'.join([alphabet[char] if char in alphabet else char for char in string1])
        window['NUMBER'].update(string2)

        if len(string1) != 0:

            if string1[0] in ['d', 't']:

                string1 = string1[1:]

        if len(string1) != 0:

            if string1[-1] in ['d', 't']:

                string1 = string1[:-1]
        
        result1 = ''.join([letter for letter in string1 if letter.lower() not in vowels])
        result2 = ""
        
        for i in result1:
            if i.lower() not in result2 and i.upper() not in result2:
                result2 += i
            
        window['RESULT'].update(result2.upper())
