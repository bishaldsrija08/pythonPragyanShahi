# WAS to make a equilatoral triangle using turtle
import turtle
t = turtle.Turtle()

a = 3
b = 100
c = 360.0/3
for i in range(3):
    t.forward(b) # Move the turtle forward by 100 units
    t.left(c) # Turn the turtle left by 120 degrees
turtle.done() # Keeps the window open until it is closed by the user