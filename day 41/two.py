# Draw two seperate shapes on the screen. eg. a square and a circle on the same canvas with out connecting them together.
import turtle
t = turtle.Turtle()

# Draw a square
for i in range(4):
    t.forward(80) # Move the turtle forward by 80 units
    t.left(90) # Turn the turtle left by 90 degrees

# Move the turtle to a new position without drawing
t.penup() # Lift the pen to avoid drawing
t.goto(150, 0) # Move the turtle to the new position (150, 0)
t.pendown() # Lower the pen to start drawing

# Draw a circle
t.circle(50) # Draw a circle with a radius of 50 units

turtle.done() # Keeps the window open until it is closed by the user