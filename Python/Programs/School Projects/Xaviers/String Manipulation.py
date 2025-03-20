a = "Python is Easy "
b = "or Hard?"
c = ["Hi", "Hello", "Bye"]
d = "23456"
e = "23as"
f="""i
love"""

print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)
print("e: ", e)
print("f: ", f)

print()

print(a+b)
print(a*4)

print()

print('Is h in a?', "h" in a)
print('Is z not in a?', "z" not in a)

print()

print('Is Hi in c?', "Hi" in c)
print('Is hi not in c?', "hi" not in c)

print()

print("Length of a: ", len(a))
print("Index of i in a: ", a.index("i"))

print()

print("Is a in Upper Case? ", a.upper().isupper())
print(a.upper())

#Same can be done for Lower Case. Use lower() and islower()

print()

print("Is d a Digit: ", d.isdigit())
print("Is a Alphabetical: ", a.isalpha())
print("Is e Alpha Numeric: ", e.isalnum())

#isalnum() doesn't accept anything other than Alphabets and Numbers, which means Spaces, Symbols etc.
#isnum() doesn't accept anything except just Numerals(Not even Spaces)
#isalpha() doesn't accept anything except just Alphabets (Not even Spaces)

print()

print("Index of love: ", f.find("love"))

#ENTER is counted in find() and index()
#"del a" would delete the variable a

print()

print("Hello, my Name is %s and I am %i Years Old."%( "Shreyas", 15))

print()

print("'Easy ' is Stripped from Right Side of a:", a.rstrip("Easy "))
print("'Python ' is Stripped from Left Side of a:", a.lstrip("Python "))
print("'  ss  ' is Stripped from Both Sides:", "  ss  ".strip(" "))

#The strip() function removes all instances of a String provided, For Eg:- Python is Easy, If we use a.rstrip("Easy "),It will remove all spaces and Letters in "Easy " until it finds a Letter which isn't in "Easy", as "s" is in "Easy ", it will also remove the "s" from "is"

print()

print('I don\'t Love VBS')

#\ Overlooks the Character next to it and Commands the Code to Skip and look for the next Quote (')

print("I don't \t Love VBS")
print("I don't\nLove VBS")

#\t provides a Tab Space
#\n is a New line Character
