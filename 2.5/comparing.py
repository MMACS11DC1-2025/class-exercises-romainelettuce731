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
similarmovie =0


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


#Find people with same movie as favourite, if this is true, add one to counter
commonmovie = input("(Reply with yes or no) \n\n").lower()
if commonmovie == "yes":
    file = open("2.4/responses.csv")
    for line in file:
        if str(userfav[4]).lower() in line.lower():
            similarmovie += 1

    #Ask if they want to see all the people with the same favourite movie
    print("Wow! "+str(similarmovie - 1)+" other people also like "+userfav[4]+"!")
    print("Would you like to see who they are?")

    #If this is yes, go through the loop again but this time, print the peoples names
    whomovie = input("(Reply with yes or no) \n\n").lower()
    if whomovie == 'yes':
        file = open("2.4/responses.csv")
        for line in file:
            if str(userfav[4]).lower() in line.lower():
                maybefriend = line.split(',')
                if maybefriend[1] == userfav[1]:
                    #do nothing lol
                    print()
                else:
                    print(maybefriend[1])
        print("You might get along well with them!")


        #If this is no, continue on
    elif whomovie == 'no':
        print("That's no good! You'll never know who they are :(")


elif commonmovie == 'no':
    print("That's too bad.")
print("Let's see where else we can find common interests!")

print("You also seem to enjoy "+userfav[8]+" movies! Do you want to see who else likes "+userfav[8]+" movies?")
commonmovie = input("(Reply with yes or no) \n\n").lower()
if commonmovie == "yes":
    file = open("2.4/responses.csv")
    for line in file:
        if str(userfav[8]).lower() in line.lower():
            similarsubj += 1

    #Ask if they want to see all the people with the same favourite subject
    print("Wow! "+str(similarsubj - 1)+" other people also like "+userfav[8]+"!")
    print("Would you like to see who they are?")

    #If this is yes, go through the loop again but this time, print the peoples names
    whosubj = input("(Reply with yes or no) \n\n").lower()
    if whosubj == 'yes':
        file = open("2.4/responses.csv")
        for line in file:
            if str(userfav[8]).lower() in line.lower():
                maybefriend2 = line.split(',')
                if maybefriend2[1] == userfav[1]:
                    #do nothing lol
                    print()
                else:
                    print(maybefriend2[1])
        print("You might get along well with them!")

    elif whomovie == 'no':
        print("You won't get to know them well!")

elif commonmovie == 'no':
    print("That's too bad.")
print("Let's compare some results!")
print(str(similarsubj)+" people also enjoy "+userfav[4]+".")
print(" and "+str(similarmovie)+"people also enjoy"+userfav[8]+".")