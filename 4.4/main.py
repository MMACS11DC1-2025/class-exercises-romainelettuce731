import turtle
turtle = turtle.Turtle()
#sets the amount of tubes that will be drawn
tubes = {2:90, 4: 180, 6: 210, 8: 45}

#asks user for input
size = int(input('How large would you like your pattern to be?'))

#if number of tubes is not 2, 4, 6, or 8, then ask user to retry
tubetrue = False
while not tubetrue:
  tubenumber = int(input("How many tubes would you like? (2, 4, 6, or 8)"))
  if tubenumber in tubes:
    tubetrue = True
  else:
    print("Sorry, that's invalid! Please try inputting a valid number (2, 4, 6, or 8)")


#set turtle speed, penup
turtle.speed(0)
turtle.penup()
      

def shape(x):
    #move the turtle
    turtle.penup()
    turtle.forward(10 + x)
     
    #draw the amount of tubes
    turtle.right(tubes[tubenumber])
    turtle.pendown()
    turtle.circle(x)
    turtle.penup()
    turtle.right(90)
    
    #if size is larger than or equal to 0, subtract 0.5 from size
    if tubenumber == 2:
      x -= 1
      shape(x)
      
    elif x > 0:
      x-= 0.5
      size*2
      shape(x)
      
    #else end drawing if sie is less than 0
    elif x <= 0:
      return 0
shape(size)

#print number of recursions (times 2 because size is subtracted by 0.5)
print("There were "+str(size)+" recursions.")