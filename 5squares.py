# Babaiar Kenzhebekov
# Date: November 6, 2025
# Problem 5: Create a pattern of squares (basic turtle example)

import turtle

t = turtle.Turtle()
t.color("blue")

for i in range(4):       # Draw square
    t.forward(100)
    t.right(90)

t.penup()
t.goto(150, 0)
t.pendown()

for i in range(4):       # Second square
    t.forward(100)
    t.right(90)

turtle.done()
