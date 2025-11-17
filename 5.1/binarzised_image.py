from PIL import Image
import is_binarized

image_pear = Image.open("5.1/pearto.jpeg").load()

image_output = Image.open('5.1/pearto.jpeg')
width = image_output.width
height = image_output.height

for i in range(width):
    for j in range(height):
        im_r = image_pear[i, j][0]
        im_g = image_pear[i, j][1]
        im_b = image_pear[i, j][2]
        if is_binarized.is_light((im_r, im_g, im_b)) == True:
            image_output.putpixel((i, j), (255, 255, 255))
        else:
            image_output.putpixel((i, j), (0, 0, 0))

image_output.save('output2.png', 'png')