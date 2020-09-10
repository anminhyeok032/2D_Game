import turtle
def gotoXY(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    
def makeNieun():
    turtle.setheading(270)
    turtle.forward(60)
    turtle.setheading(0)
    turtle.forward(60)

gotoXY(-250, 0)
turtle.circle(50)


gotoXY(-150, 0)
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(270)
turtle.forward(50)
turtle.setheading(0)
turtle.forward(50)

gotoXY(-200,-25)
makeNieun()

gotoXY(-50,0)
i = 0
while i < 4: 
    turtle.forward(60)
    turtle.left(90)
    i += 1

gotoXY(50, -15)
turtle.left(90)
turtle.forward(90)

gotoXY(0, -25)
makeNieun()

gotoXY(150, 120)
turtle.right(30)
turtle.forward(40)
gotoXY(130, 80)
turtle.setheading(0)
turtle.forward(100)

gotoXY(180, 0)
turtle.circle(35)

gotoXY(250, -20)
turtle.setheading(90)
turtle.forward(100)
j = 0
while j < 2:
    turtle.setheading(270)
    turtle.forward(30)
    turtle.setheading(180)
    turtle.forward(30)
    turtle.setheading(0)
    turtle.forward(30)
    j += 1

gotoXY(160, -25)
turtle.setheading(0)
turtle.forward(70)
turtle.right(90)
turtle.forward(60)

turtle.exitonclick()

