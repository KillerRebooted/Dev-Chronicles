'''n = int(input("enter num: "))
a=0
b=1
print (a)
print (b)
for i in range(1,n+1):
    c=a+b
    print(c)
    a=b
    b=c'''

'''num = int(input("enter num to factorise: "))
b=1
for i in range(1,num+1):
    b=b*i
print (b)'''


'''def add():
    # Defining local variables. They has scope only within a function
    a = 20
    b = 30
    c = a + b
    print("The sum is:", c)

    
add()'''

'''# Program to show the use of keywords for, while, break, continue  
for i in range(15):  
    
    print( i + 4, end = " ")  
        
    # breaking the loop when i = 9  
    if i == 9:  
        break     
print() 
        
# looping from 1 to 15  
i = 0 # initial condition  
while i < 15:  
        
    # When i has value 9, loop will jump to next iteration using continue. It will not print  
    if i == 9:  
        i += 3  
        continue  
    else:  
        # when i is not equal to 9, adding 2 and printing the value  
        print( i + 2, end = " ")  
            
    i += 1''' 


import time
print("hello", flush=True)

time.sleep(5)