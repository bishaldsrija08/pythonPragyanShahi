import turtle
t = turtle.Turtle()
a = 5
b= 50
c = 360.0/a
for i in range(a):
    t.forward(b)
    t.left(c)
turtle.done() # Keeps the window open until it is closed by the user