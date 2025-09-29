"""
Create a program that uses comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You may use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.

------------------------------------------------------------------------------------
Reccomendation bot that suggests people with similar interests you may want to be
friends with

"""
#Initialize variables
similarsubj = 0


#Open the file
file = open("2.4/responses.csv")

#Greet user
print("Hello! What is your name?")

#Grab user data from file
user = input().lower()
for line in file:
    if user in line.lower():
        userfav = line.split(",")
        print("Hello, "+ userfav[1]+". \n")

#add error later

#Find favourite subject, ask if user wants to see people with same favourite subject
print("It appears that you enjoy "+userfav[4]+". Would you like to see ")
print("people who also enjoy "+userfav[4]+"?")

if input("(Reply with yes or no) \n\n").lower() == "yes":
    for line in file:
        if str(userfav[4]).lower() in line.lower():
            similarsubj += 1
            print(str(similarsubj))



