file = open("6.2/spotify.csv")
junk = file.readline()
count = 0
song_data = []
artist_data = []
name_data = []
userInput = False
while not userInput:
    choice = input("Hi! I'm music bot. Would you like a playlist with dancability or energy?").lower()
    if choice == "energy" or choice == "dancability":
        userInput = True
    else:
        print("Please try again.")

for line in file:
    items = line.strip().split(",")
    artist = str(items[-1])
    songtitle = str(items[-2])
    artist_data.append(artist)
    name_data.append(songtitle)
    if choice == 'energy':
        choicedata = float(items[3])
        song_data.append(choicedata)
    else:
        choicedata = float(items[1])
        song_data.append(choicedata)

for i in range(len(song_data)):
    highest_score = song_data[i]
    highest_index = i
    for j in range(i+1, len(song_data)):
        if song_data[j] > highest_score:
            highest_score = song_data[j]
            highest_index = j
        song_data[highest_index], song_data[i] = song_data[i], song_data[highest_index]
        name_data[highest_index], name_data[i] = name_data[i], name_data[highest_index]
        artist_data[highest_index], artist_data[i] = artist_data[i], artist_data[highest_index]
if choice == 'energy':
        print('Energy score \tSong')
        print(str(song_data[0]) + "\t" + name_data[0] + " by " + artist_data[0])
        print(str(song_data[1]) + "\t" + name_data[1] + " by " + artist_data[1])
        print(str(song_data[2]) + "\t" + name_data[2] + " by " + artist_data[2])
        print(str(song_data[3]) + "\t" + name_data[3] + " by " + artist_data[3])
        print(str(song_data[4]) + "\t" + name_data[4] + " by " + artist_data[4])
else:
        print('Dance score \tSong')
        print(str(song_data[0]) + "\t" + name_data[0] + " by " + artist_data[0])
        print(str(song_data[1]) + "\t" + name_data[1] + " by " + artist_data[1])
        print(str(song_data[2]) + "\t" + name_data[2] + " by " + artist_data[2])
        print(str(song_data[3]) + "\t" + name_data[3] + " by " + artist_data[3])
        print(str(song_data[4]) + "\t" + name_data[4] + " by " + artist_data[4])