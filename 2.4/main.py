file = open("2.4/responses.csv")
<<<<<<< HEAD
count = 0
cat = 0
for line in file:
    count+=1
    if "mason" in line.lower():
        print(line)
        print("Mason is found on line "+str(count))
        
    if "cat" in line.lower():
        cat+=1

print(str(cat)+ " people like cats.")

    
=======
>>>>>>> upstream/HEAD
