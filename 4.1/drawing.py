"""
Make An Interactive Drawing or Animation 
Explore the turtle drawing package to create an interactive drawing.
It should use a while loop.
Your program should also include at least one function you’ve made yourself 
"""
import turtle
turty = turtle.Turtle()

turty.speed(0)
size = int(input("How big do you want your saw pattern to be?"))
num = int(input("How many saws do you want?"))
count = 0
while True:
    def spike(x,y):
      turty.forward(50)
      for i in range(100):
        turty.forward(20 + size)
        turty.right(75 + size)
        turty.forward(10 + size)
        turty.stamp()
    spike(1, 1)
    turty.penup()
    turty.forward(50)
    turty.pendown()
    count += 1
    size = size
    
    if count == num:
      break
