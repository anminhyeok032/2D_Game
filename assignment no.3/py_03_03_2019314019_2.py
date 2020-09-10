import turtle

def gotoXY(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def square(a):
    turtle.setheading(270)
    turtle.forward(a)
    turtle.setheading(0)
    turtle.forward(a)
    turtle.setheading(90)
    turtle.forward(a)
    turtle.setheading(180)
    turtle.forward(a)

def mini(b):
    turtle.setheading(0)
    turtle.forward(b)
    turtle.setheading(90)
    turtle.forward(b)

gotoXY(-300, 300)
square(500)

y = 200
while (y > - 300):
    x = -300
    while(x < 200):
        gotoXY(x, y)
        mini(100)
        x += 100
    y += -100


turtle.exitonclick()
