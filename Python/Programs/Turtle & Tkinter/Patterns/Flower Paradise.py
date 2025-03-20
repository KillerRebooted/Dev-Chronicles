from turtle import *

win = Screen()
win.title("Flower Paradise")
win.bgcolor("white")

Flower = Turtle()
Flower.speed(0)

num1 = 10
num2 = 10

for i in range(500):
    
    Flower.circle(num1)
    Flower.circle(-num1)
    Flower.left(num2)

    if i%10 == 0:
            
        num1 += 10
        
    num2 += 10

done()