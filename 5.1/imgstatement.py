import time
t0 = time.time()
from PIL import Image

def colour(r, g, b):
    if r >= 158 and g >= 158 and b >= 158:
        return "bright"
    elif r <= 127 and g <= 127 and b <= 127:
        return "dark"
        
file = Image.open("5.1/pearto.jpeg")
pear_image = file.load()

brightpix = []
darkpix = []

width = file.width
height = file.height

t1 = time.time()

for x in range(width):
    for y in range(height):
        pixel_r = pear_image[x, y][0]
        pixel_g = pear_image[x,y][1]
        pixel_b = pear_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "bright":
            brightpix.append(pear_image[x,y])

        if colour(pixel_r, pixel_g, pixel_b) == "dark":
            darkpix.append(pear_image[x,y])



t2 = time.time()

num_br = len(brightpix)
num_dr = len(darkpix)


total_pixels = width*height
bright_percent = (num_br / total_pixels)*100
dark_percent = (num_dr / total_pixels)  * 100

report = "There are {:.2f} % .bright pixels. ".format(bright_percent) + "There are {:.2f}% .dark pixels.".format(dark_percent)
print(report)
file.save('output3.png', 'png')

t3 = time.time()

module_load = t1-t0
loop = t2-t1
calculate = t3-t2
all = t3-t0
timings = "It took {:.2f}s to import PIL and open the image, {:.2f}s to perform the loop, and {:.2f}s to calculate the total. It took {:.2f}s in total.".format(module_load, loop, calculate, all)

if bright_percent > dark_percent:
    print("The image is bright.")

elif dark_percent > bright_percent:
    print("The image is dark.")