import time
t0 = time.time()
from PIL import Image

def colour(r, g, b):
    if r > 150 and g > 150 and b < 150:
        return "yellow"
    elif r > 107 and g < 47 and b < 35:
        return "red"
    elif r < 95 and g < 148 and b > 95:
        return 'blue'
    elif r < 66 and g > 21 and b < 42:
        return 'green'
    elif r > 24 and g < 174 and b > 21:
        return 'purple'
file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()

yellow_pixels = []
redp = []
bluep = []
greenp = []
purplep = []

width = file.width
height = file.height

t1 = time.time()

for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x, y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellow_pixels.append(jb_image[x,y])
            file.putpixel((x, y), (255, 255, 255))

        if colour(pixel_r, pixel_g, pixel_b) == "red":
            redp.append(jb_image[x,y])

        elif colour(pixel_r, pixel_g, pixel_b) == "blue":
            bluep.append(jb_image[x,y])

        elif colour(pixel_r, pixel_g, pixel_b) == "purple":
            purplep.append(jb_image[x,y])

        elif colour(pixel_r, pixel_g, pixel_b) == "green":
            greenp.append(jb_image[x,y])


t2 = time.time()

num_yellow = len(yellow_pixels)
num_red = len(redp)
num_blue = len(bluep)
num_green = len(greenp)
num_purple = len(purplep)

total_pixels = width*height
yellow_ratio = num_yellow / total_pixels
red_percent = (num_red / total_pixels)  * 100
blue_percent = (num_blue / total_pixels)  * 100
green_percent = (num_green / total_pixels)  * 100
purple_percent = (num_purple / total_pixels)  * 100

yellow_percent = yellow_ratio * 100
report = "There are {:.2f}% yellow jellybeans.".format(yellow_percent) + "There are {:.2f}% .red jellybeans.".format(red_percent) + "There are {:.2f}% .green jellybeans.".format(green_percent) + "There are {:.2f}% .blue jellybeans.".format(blue_percent) + "There are {:.2f}% purple jellybeans.".format(purple_percent)
print(report)
file.save('output.png', 'png')

t3 = time.time()

module_load = t1-t0
loop = t2-t1
calculate = t3-t2
all = t3-t0
timings = "It took {:.2f}s to import PIL and open the image, {:.2f}s to perform the loop, and {:.2f}s to calculate the total. It took {:.2f}s in total.".format(module_load, loop, calculate, all)
print(timings)
