from PIL import Image

def colour(r, g, b):
    #yellow
    if r > 150 and g > 150 and b < 150:
        return "yellow"
    else:
        return "other"
    
file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()

yellow_pixels = []

width = file.width
height = file.height

for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x, y][0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]

        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            yellow_pixels.append(jb_image[x,y])
            file.putpixel((x, y), (255, 255, 255))

num_yellow = len(yellow_pixels)

total_pixels = width*height
yellow_ratio = num_yellow / total_pixels
yellow_percent = yellow_ratio * 100
report = "There are {:.2f}% yellow jellybeans.".format(yellow_percent)
print(report)
file.save('output.png', 'png')