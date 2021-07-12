import turtle
turtle.shape('turtle')
x = 4
d = 10
while x > 0:
    turtle.left(90)
    turtle.forward(d)
    x -= 1
    if x == 0:
        turtle.right(45)
        turtle.penup()
        turtle.forward(13)
        turtle.left(45)
        turtle.pendown()
        x += 4
        d += 20
