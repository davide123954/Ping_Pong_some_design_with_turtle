'''

#To design some stars 
import turtle
a= turtle.Turtle()
a.getscreen().bgcolor("black")

a.penup()
a.goto(-200, 100)
a.pendown()
a.color("yellow")

a.speed(25)
def star(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
            turtle.end_fill()
star(a,360)
turtle.done()
'''
'''
from turtle import*
color('blue','red')
begin_fill()
while True:
    forward(300)
    left(170)
    if abs(pos())<1:
        break
end_fill()
done()
'''
'''
from turtle import*
import random
speed(speed='fastest')
def drawn(n,x,angle):
    for i in range(n):
        colormode(255)
        a= random.randint(0,255)
        b= random.randint(0,255)
        c= random.randint(0,255)
        pencolor(a,b,c)
        fillcolor(a,b,c)
        begin_fill()
        for j in range(5):
            forward(5*n-5*i)
            right(x)
            forward(5*n-5*i)
            right(72-x)
        end_fill()
        rt(angle)
n=30
x=144
angle=18
drawn(n,x,angle)
'''
'''
#To design a square
import turtle

silly = turtle.Turtle()
silly.forward(50)
silly.right(90)     

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

turtle.done()
'''
'''
#To design a star
import turtle 
star = turtle.Turtle()
for i in range(50):
    star.forward(105)
    star.right(144)
    
turtle.done()
'''
'''
#To design other beutiful form
import turtle 
painter = turtle.Turtle()
painter.pencolor("blue")
for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()
'''
'''
#To design other cool form
import turtle 

ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()
'''
'''
#To design other cool form
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(180):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
'''
'''
#To design some name like "IDAN"
from turtle import Turtle, Screen

NAME = "IDAN"

BORDER = 1
BOX_WIDTH, BOX_HEIGHT = 6, 10  # letter bounding box
WIDTH, HEIGHT = BOX_WIDTH - BORDER * 2, BOX_HEIGHT - BORDER * 2  # letter size

def letter_A(turtle):
    turtle.forward(HEIGHT / 2)
    for _ in range(3):
        turtle.forward(HEIGHT / 2)
        turtle.right(90)
        turtle.forward(WIDTH)
        turtle.right(90)
    turtle.forward(HEIGHT)

def letter_D(turtle):
    turtle.forward(HEIGHT)
    turtle.right(90)
    turtle.circle(-HEIGHT / 2, 180, 30)

def letter_I(turtle):
    turtle.right(90)
    turtle.forward(WIDTH)
    turtle.backward(WIDTH / 2)
    turtle.left(90)
    turtle.forward(HEIGHT)
    turtle.right(90)
    turtle.backward(WIDTH / 2)
    turtle.forward(WIDTH)

def letter_N(turtle):
    turtle.forward(HEIGHT)
    turtle.goto(turtle.xcor() + WIDTH, BORDER)
    turtle.forward(HEIGHT)

LETTERS = {'A': letter_A, 'D': letter_D, 'I': letter_I, 'N': letter_N}

wn = Screen()
wn.setup(800, 400)  # arbitrary
wn.title("Turtle writing my name: {}".format(NAME))
wn.setworldcoordinates(0, 0, BOX_WIDTH * len(NAME), BOX_HEIGHT)

marker = Turtle()

for counter, letter in enumerate(NAME):
    marker.penup()
    marker.goto(counter * BOX_WIDTH + BORDER, BORDER)
    marker.setheading(90)

    if letter in LETTERS:
        marker.pendown()
        LETTERS[letter](marker)

marker.hideturtle()

wn.mainloop()
'''
'''
#To design some simple string with cool style
import turtle
turtle.color('blue')
style = ('Arial', 30, 'italic')
turtle.write('Davide 🤑', font=style, align='center')
turtle.hideturtle()
'''
'''
#To design a tree
import turtle
hr = turtle.Turtle()
hr.left(90)
hr.speed(150)

def tree(i):
    if(i>=20):
      hr.forward(i)
      hr.left(30)
      tree(3*i/4)
      hr.right(30)
      tree(3*i/4)
      hr.right(30)
      tree(3*i/4)
      hr.left(30)
      hr.backward(i)

tree(100)
turtle.done()
'''













