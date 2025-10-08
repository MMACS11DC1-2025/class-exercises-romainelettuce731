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

Example: Ask the user if they would like to see people with similar interests
If they say yes, display a counter and ask if they want to see specific names
If this is no, do not add to counter and skip ahead

If the response is invalid, provide error message and continue forwards.
If username is not in database, provide error and quit program

"""
#Initialize variables
similarsubj = 0
similarmovie = 0

usernotindatabase = 0


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
        break
    else:
        usernotindatabase += 1

print(usernotindatabase)

if usernotindatabase >= 28:
    quit("I'm sorry, I couldn't find your name in the database. Please try again.")
    

#Find favourite subject, ask if user wants to see people with same favourite subject
print("It appears that you enjoy "+userfav[4]+". Would you like to see ")
print("people who also enjoy "+userfav[4]+"?")


#Find people with same subject as favourite, if this is true, add one to counter
commonsubj = input("(Reply with yes or no) \n\n").lower()
if commonsubj == "yes":
    file = open("2.4/responses.csv")
    for line in file:
        if str(userfav[4]).lower() in line.lower():
            similarsubj += 1

     #If amount of people greater than 0 (1 subtracted by self) enjoys same subject
    if similarsubj > 1:
        
        #Ask if they want to see all the people with the same favourite subject
        print("Wow! "+str(similarsubj - 1)+" other people also like "+userfav[4]+"!")
        print("Would you like to see who they are?")

        #If this is yes, go through the loop again but this time, print the peoples names
        whosubj = input("(Reply with yes or no) \n\n").lower()
        if whosubj == 'yes':
            file = open("2.4/responses.csv")
            for line in file:
                if str(userfav[4]).lower() in line.lower():
                    maybefriend = line.split(',')
                    if maybefriend[1] == userfav[1]:
                        #If you are your own friend, don't print your own name
                        print()
                    else:
                        print(maybefriend[1])
            print("\nYou might get along well with them!")


            #If this is no, continue on
        elif whosubj == 'no':
            print("That's no good! You'll never know who they are :(")
    elif similarsubj <= 1:
        print("Nobody else seems to enjoy "+ userfav[4]+" :(")

elif commonsubj == 'no':
    similarsubj -= 1
    print("That's too bad.")

else:
    print("I'm sorry, but I didn't understand what you said. Let's move forwards.")
    similarmovie -= 1
print("Let's see where else we can find common interests!\n")

print("You also seem to enjoy "+userfav[8]+" movies! Do you want to see who else likes "+userfav[8]+" movies?")
commonmovie = input("(Reply with yes or no) \n\n").lower()
if commonmovie == "yes":
    file = open("2.4/responses.csv")
    for line in file:
        if str(userfav[8]).lower() in line.lower():
            similarmovie += 1

    #If amount of people greater than 0 (1 subtracted by self) enjoys same movie
    if similarmovie > 1:
        #Ask if they want to see all the people with the same favourite movie
        print("Wow! "+str(similarmovie - 1)+" other people also like "+userfav[8]+"!")
        print("Would you like to see who they are?")


        #If this is yes, go through the loop again but this time, print the peoples names
        whomovie = input("(Reply with yes or no) \n\n").lower()
        if whomovie == 'yes':
            file = open("2.4/responses.csv")
            for line in file:
                if str(userfav[8]).lower() in line.lower():
                    maybefriend2 = line.split(',')
                    if maybefriend2[1] == userfav[1]:
                        #If you are your own friend, don't print your own name
                        print()
                    else:
                        print(maybefriend2[1])
            print("\nYou might get along well with them!")

        elif whomovie == 'no':
            print("You won't get to know them well!")
    elif similarmovie <= 1:
        print("Nobody else seems to enjoy "+ userfav[8]+" movies :(")

elif commonmovie == 'no':
    similarmovie -= 1
    print("That's too bad.")
else:
    print("I'm sorry, but I didn't understand what you said. Let's move forwards.")
    similarmovie -= 1

#Show user individual results and total amount of potential friends.
print("Let's compare some results! \n\n\n")

#Remove self from other user count
if similarsubj > 0:
    similarsubj -= 1
if similarmovie > 0:
    similarmovie -= 1


#Tally scores, if score is set to negative, reset score to 0 for adding purposes,
#reply sadly :(
if similarsubj >= 0:
    print(str(similarsubj)+" people also enjoy "+userfav[4]+".")
else: 
    print("You never let me find how many people also enjoy "+userfav[4]+". :(")
    similarsubj = 0

if similarmovie >= 0:
    print(str(similarmovie)+" people also enjoy "+userfav[8]+".")
else: 
    print("You never let me find how many people also enjoy "+userfav[8]+". :(")
    similarmovie = 0

if (similarmovie+similarsubj) >= 0:
    print("That's "+str(similarsubj + similarmovie)+" new people that you could be friends with!")

