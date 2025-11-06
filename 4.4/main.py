import turtle
turtle = turtle.Turtle()

#sets the amount of tubes that will be drawn
tubes = {2:90, 4: 180, 6: 210, 8: 45}

#use this to convert to str, otherwise tubes dictionary doesn't behave well 
#reference tubes later, use this as a 'checkpoint' or 'border control' for error handling
tubelist = [2,4,6,8]

#asks user for input
sizecheck = False

#checks to make sure an integer is inputted
while not sizecheck:
  numbers = []
  size = input(('How large would you like your pattern to be?')).strip()
  
  #create a list of numbers between 0 and 300
  for i in range(301):
    numbers += [i]
    
  #if the number is in the list (between 0 and 300) and isn't blank, then convert to int and check True
  if size in str(numbers) and size != "":
    size = int(size)
    sizecheck = True
  else:
    print("Please enter a whole integer less than 300")

#if number of tubes is not 2, 4, 6, or 8, then ask user to retry
tubecheck = False

#checks to make sure an integer within the tubes dictionary is inputted
while not tubecheck:
  tubenumber = input("How many tubes would you like? (2, 4, 6, or 8)").strip()
  
  #use tubeslist to convert to string because if dictionary is converted to a string, it behaves weirdly :(
  #if the input is not blank and is in tubelist, check True and convert to an integer
  if str(tubenumber) != "" and tubenumber in str(tubelist):
    tubenumber = int(tubenumber)
    tubecheck = True
  else:
    print("Sorry, that's invalid! Please try inputting a valid number (2, 4, 6, or 8)")


#-----------------------------------------------------------------------

#set turtle speed, penup
turtle.speed(0)
turtle.penup()
      

def shape(x):
    #move the turtle
    turtle.penup()
    turtle.forward(10 + x)
     
    #draw the amount of tubes
    #reference tubes here
    turtle.right(tubes[tubenumber])
    turtle.pendown()
    turtle.circle(x)
    turtle.penup()
    turtle.right(90)
    
    #if there are two tubes, subtract 1 from size to keep ring spacing not too close
    if tubenumber == 2 and x > 0:
      x -= 1
      shape(x)
    
    #elif there are more than two tubes, subtract by 0.5 for more even distribution of rings among tubes
    elif x > 0:
      x-= 0.5
      size*2
      shape(x)
      
    #else end drawing if sie is less than 0
    elif x <= 0:
      return 0
shape(size)

#print number of recursions 
if tubenumber == 2:
  print("There were "+str(size)+" recursions.")
  
#times 2 because size is subtracted by 0.5
else:
  print("There were "+str(size*2)+" recursions.")