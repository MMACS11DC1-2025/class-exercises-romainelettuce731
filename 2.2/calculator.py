"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish. Remember to design your 
algorithm in English first, then translate it to Python 
code. Test as you go!
"""

#calculator
#mason lui
#sept 22

print("CALCULATOR RUNNING SUCCESSFULLY")
print("ENTER FIRST NUMBER")
num1 = float(input())

print("ENTER OPERATOR")
operator = input()

print("ENTER SECOND NUMBER")
num2 = float(input())

if operator == '+':
  print('YOUR ANSWER IS '+str(num1 + num2))

elif operator == '-':
  print('YOUR ANSWER IS '+str(num1 - num2))

elif operator == '*':
  print('YOUR ANSWER IS '+str(num1 * num2))

elif operator == '/':
  print('YOUR ANSWER IS '+str(num1 / num2))

else:
  print("SYNTAX ERROR")
