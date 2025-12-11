from PIL import Image
import time

t0 = time.time()

#define the lists that will be used
pixelart = []
pixelartlen = []
brushart = []
brushartlen = []
numlist = []

inputcheck = False

#this is the function that counts the amount of unique colours in the image
#this is my is_target_data
def pixel_art_check(imgname):
    #open image, get the data
    inp_img = Image.open(imgname)
    pixels = inp_img.getdata()

    #set creates a list and removes all duplicates within the list
    uniquecolors = set(pixels)
    count = (len(uniquecolors))
    return count

#this is the function that determines which list each piece of data should go in
def list_append(imgname, pixcount, pixelart, pixelartlen, brushart, brushartlen):
    #if there are less than 100 000 unique colours in an image,
    #it is determined to be a pixel art image
    if pixcount <= 100000:
        pixelart.append(imgname)
        pixelartlen.append(pixcount)
    #if it has more than 100 000, it is determined to be a brush art image
    else:
        brushart.append(imgname)
        brushartlen.append(pixcount)



#------------------------------------------------------------------------
#use the functions on each image
#this function runs through the images and determines the results of the data
def give_results(img):
    count = pixel_art_check(img)
    list_append(img, count, pixelart, pixelartlen, brushart, brushartlen)
t1 = time.time()

give_results('6.7/Deltarune-poster.png')
t2 = time.time()

give_results('6.7/Undertale_Cast.png')
t3 = time.time()

give_results('6.7/asrielfight.webp')
t4 = time.time()

give_results('6.7/hatsune-miku.jpg')
t5 = time.time()

give_results('6.7/starrynight.jpg')
t6 = time.time()

give_results('6.7/frisksprite.png')
t7 = time.time()

give_results('6.7/deltaruneposterart.jpg')
t8 = time.time()

give_results('6.7/lastsupper.jpg')
t9 = time.time()

give_results('6.7/titan.jpg')
t10 = time.time()

give_results('6.7/mario.jpg')
t11 = time.time()

#-----------------------------------------------------------------------------------
#implemented selection sort to sort from highest to lowest pxiel count
def select_sort(list1, list2):
    for i in range(len(list1)):
        highest_score = list1[i]
        highest_index = i
        for j in range(i+1, len(list1)):
            if list1[j]> highest_score:
                highest_score = list1[j]
                highest_index = j
        list1[highest_index], list1[i] = list1[i], list1[highest_index]
        list2[highest_index], list2[i] = list2[i], list2[highest_index]

select_sort(pixelartlen, pixelart)
select_sort(brushartlen, brushart)

#add both lists to a master list from highest unique colours to lowest
masterlistlen = brushartlen+pixelartlen
masterlist = brushart+pixelart
mastersum = 0
for i in range(len(masterlistlen)):
    mastersum += masterlistlen[i]

#-------------------------------------------------------------------------------------
def binary_search(data_list, targetscore):
    search_start_index = 0
    search_end_index = len(data_list)-1
    targetscoremin = targetscore - 20000
    targetscoremax = targetscore + 20000
    while search_start_index <= search_end_index:
        midpoint = int((search_start_index+search_end_index)/2)
        if data_list[midpoint] >= targetscoremin and data_list[midpoint]<= targetscoremax:
            return data_list[midpoint], masterlist[midpoint]
        elif data_list[midpoint] < targetscore:
            search_start_index = midpoint+1
        else:
            search_end_index = midpoint-1
    return -1


#-------------------------------------------------------------------------------------
#print the pixel results
for i in range(5):
    print('{} had {} unique colours.'.format(pixelart[i], pixelartlen[i])), print('{} had {} unique colours.'.format(brushart[i], brushartlen[i]))


#print the top 5 images with most unique colours
print('\n')
print("The top 5 images with the most unique colours were:")
print("# of colours \tFilename")

#use master list to print the top 5 images with the most unique colours
for i in range(len(masterlist[:5])):
    print(str(masterlistlen[i]) +'\t\t'+ masterlist[i])

print('\n')

#print the results  of the binary search
binarysearchresult = binary_search(masterlistlen, 150000)
print("The first image found within the binary search range (130 000 to 170 000) was "+binarysearchresult[1]+". It has "+str(binarysearchresult[0])+" unique colours.")
print('\n')

#print the time results
print('Loading the functions and modules as well as waiting for user input took {:.3f} seconds. The first image took {:.3f} seconds, the second image took {:.3f} seconds, the third image took {:.3f} seconds,'.format(t1-t0, t2-t1, t3-t2, t4-t3,))
print('the fourth image took {:.3f} seconds, the fifth image took {:.3f} seconds, the sixth image took {:.3f} seconds, the seventh image took {:.3f} seconds,'.format(t5-t4, t6-t5, t7-t6, t8-t7))
print('the eigth image took {:.3f} seconds, the ninth image took {:.3f} seconds, and the last image took {:.3f} seconds.'.format(t9-t8, t10-t9, t11-t10))
print('In total, the program took {:.3f} seconds to run.\n\n'.format(t11-t0))

#print the results of pixel art vs brush art
print("Here are the results for which images were determined to be pixel art and which ones were brush art.")
print("Brush art \t\t\t\t\tPixel art")
for i in range(5):
    print(brushart[i] +'\t\t\t\t'+ pixelart[i])