import tkinter as tk

index = -1

def button_press(num):

    global index

    entry.insert(tk.END, str(num))

    value = entry.get()

    index += 1
    
    try:
        temp = value[:-1]
        temp = value.removeprefix(temp)
        
        temp2 = value[:-2]
        temp2 = value.removeprefix(temp2)
        temp2 = temp2[0]

    except:

        temp = value
        temp2 = "0"

    if temp.isdigit():
        
        entry.insert(tk.END, "")

    elif (temp.isdigit() == False) and (temp2.isdigit()):

        entry.insert(tk.END, "")

    elif (temp.isdigit() == False) and (temp2.isdigit() == False):

        entry.delete(index)
        index -= 1


def backspace():
    
    global index

    temp = entry.get()
    temp = temp[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, temp)

    index -= 1

    if index < 0:

        index = -1

def clear():

    global index

    index = -1
    entry.delete(0, tk.END)

def equal():

    value = entry.get()

    if value[-1].isdigit() == False:

        value = value[:-1]

    entry.delete(0, tk.END)
    entry.insert(0, f"{value} = {eval(value)}")
            

win = tk.Tk()
win.title("Simple Calculator")
win.geometry("500x500+550+150")

greeting = tk.Label(text = "Simple Calculator", font = ("Courier", 20, "bold", "italic"))
greeting.pack()

entry = tk.Entry(width = 30, justify = 'center')
entry.place(x = 160, y = 150)

_clear = tk.Button(text = "Clear", height = 2, width = 10, command = clear, activebackground = "red")
_clear.place(x = 70, y = 140)

_backspace = tk.Button(text = "Backspace", height = 2, width = 10, command = backspace, activebackground = "red")
_backspace.place(x = 360, y = 140)

_1 = tk.Button(text = "1", height = 2, width = 5, command = lambda: button_press(1), activebackground = "red")
_1.place(x = 155, y = 200)

_2 = tk.Button(text = "2", height = 2, width = 5, command = lambda: button_press(2), activebackground = "red")
_2.place(x = 205, y = 200)

_3 = tk.Button(text = "3", height = 2, width = 5, command = lambda: button_press(3), activebackground = "red")
_3.place(x = 255, y = 200)

_divide = tk.Button(text = "/", height = 2, width = 5, command = lambda: button_press("/"), activebackground = "red")
_divide.place(x = 305, y = 200)

_4 = tk.Button(text = "4", height = 2, width = 5, command = lambda: button_press(4), activebackground = "red")
_4.place(x = 155, y = 250)

_5 = tk.Button(text = "5", height = 2, width = 5, command = lambda: button_press(5), activebackground = "red")
_5.place(x = 205, y = 250)

_6 = tk.Button(text = "6", height = 2, width = 5, command = lambda: button_press(6), activebackground = "red")
_6.place(x = 255, y = 250)

_multiply = tk.Button(text = "*", height = 2, width = 5, command = lambda: button_press("*"), activebackground = "red")
_multiply.place(x = 305, y = 250)

_7 = tk.Button(text = "7", height = 2, width = 5, command = lambda: button_press(7), activebackground = "red")
_7.place(x = 155, y = 300)

_8 = tk.Button(text = "8", height = 2, width = 5, command = lambda: button_press(8), activebackground = "red")
_8.place(x = 205, y = 300)

_9 = tk.Button(text = "9", height = 2, width = 5, command = lambda: button_press(9), activebackground = "red")
_9.place(x = 255, y = 300)

_subtract = tk.Button(text = "-", height = 2, width = 5, command = lambda: button_press("-"), activebackground = "red")
_subtract.place(x = 305, y = 300)

_0 = tk.Button(text = "0", height = 2, width = 5, command = lambda: button_press("0"), activebackground = "red")
_0.place(x = 155, y = 350)

_equal = tk.Button(text = "=", height = 2, width = 12, command = equal, activebackground = "red")
_equal.place(x = 205, y = 350)

_add = tk.Button(text = "+", height = 2, width = 5, command = lambda: button_press("+"), activebackground = "red")
_add.place(x = 305, y = 350)

win.mainloop()