file = open("6.2/spotify.csv")
junk = file.readline()
count = 0
drake_data = []

for line in file:
	items = line.strip().split(",")
	artist = str(items[-1])
	songtitle = str(items[-2])
	danceability = float(items[1])
	
	if artist == "Drake":
		drake_data.append([danceability, songtitle, artist])

for i in range(len(drake_data)):
	largest_score = drake_data[i]
	largest_index = i
	for j in range(i+1, len(drake_data)):
		if drake_data[j] > largest_score:
			largest_score = drake_data[j]
			largest_index = j

	drake_data[largest_index], drake_data[i] = drake_data[i], drake_data[largest_index]
print("The top 5 dancable Drake songs are:")
print("Dance score \tSong")
for item in drake_data[:5]:
	print(str(item[0]) + "\t\t" + item[1] + " by " + item[2])