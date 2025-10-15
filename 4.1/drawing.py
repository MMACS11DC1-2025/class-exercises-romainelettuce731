"""
Make An Interactive Drawing or Animation 
Explore the turtle drawing package to create an interactive drawing.
It should use a while loop.
Your program should also include at least one function you’ve made yourself 
"""
import turtle
turty = turtle.Turtle()

turty.speed(0)
size = input("How big do you want your smiley saw to be?")
size = int(size)
count = 0
while True:
    def spike(x,y):
      for i in range(100):
        turty.forward(10 + size)
        turty.right(90 + size)
        turty.forward(10 + size)
    spike(1, 1)
    turty.penup()
    turty.forward(50 + size)
    turty.pendown()
    count += 1
    
    if count == 6:
      break