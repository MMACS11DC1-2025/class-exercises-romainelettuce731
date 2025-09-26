file = open("2.4/responses.csv")
for i in file:
    if "mason" in line.lower():
        print(line)
    
