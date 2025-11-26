from PIL import Image
import time


colorlist = []

def is_pixel(r, g, b):
    rgb = str(r)+str(g)+str(b)
    if rgb not in colorlist:
        colorlist.append(rgb)
    else:
        return



inp_img1 = Image.open('6.7/Deltarune-poster.png').load()

currentimg = Image.open('6.7/Deltarune-poster.png')
width = currentimg.width
height = currentimg.height

for i in range(width):
    for j in range(height):
        im_r = currentimg[i, j][0]
        im_g = currentimg[i, j][1]
        im_b = currentimg[i, j][2]
        if is_pixel((im_r, im_g, im_b)) == True:
            currentimg.putpixel((i, j), (255, 255, 255))
        else:
            currentimg.putpixel((i, j), (0, 0, 0))
    