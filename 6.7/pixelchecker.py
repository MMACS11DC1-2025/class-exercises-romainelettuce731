from PIL import Image
import time

t0 = time.time()

#define the lists that will be used
pixelart = []
pixelartlen = []
brushart = []
brushartlen = []

#this is the function that counts the amount of unique colours in the image
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

#print the lists
print("Pixel art = "+str(pixelart))
print("Pixel art pixel count = "+str(pixelartlen))
print('\n')

print("Brush art = "+str(brushart))
print("Brush art pixel count = "+str(brushartlen))
print('\n')

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
print(pixelartlen, pixelart)

select_sort(brushartlen, brushart)
print(brushartlen, brushart)
print('\n')

#print the time results
print('Loading the functions and modules took {:.2f} seconds. The first image took {:.2f} seconds, the second image took {:.2f} seconds, the third image took {:.2f} seconds,'.format(t1-t0, t2-t1, t3-t2, t4-t3,))
print('the fourth image took {:.2f} seconds, the fifth image took {:.2f} seconds, the sixth image took {:.2f} seconds, the seventh image took {:.2f} seconds,'.format(t5-t4, t6-t5, t7-t6, t8-t7))
print('the eigth image took {:.2f} seconds, the ninth image took {:.2f} seconds, and the last image took {:.2f} seconds.'.format(t9-t8, t10-t9, t11-t10))
print('In total, the program took {:.2f} seconds to run.'.format(t11-t0))