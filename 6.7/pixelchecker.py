from PIL import Image
import time

t0 = time.time()

colorlist = []

def is_pixel(r, g, b):
    rgb = (r, g, b)
    if rgb not in colorlist:
        colorlist.append(rgb)
        return True
    else:
        return False

def pixel_art_check(imgname):
    inp_img = Image.open(imgname)
    width = inp_img.width
    height = inp_img.height
    currentimg = Image.open(imgname).load()
    for i in range(width):
        for j in range(height):
            im_r = currentimg[i, j][0]
            im_g = currentimg[i, j][1]
            im_b = currentimg[i, j][2]
            is_pixel(im_r, im_g, im_b)
    inp_img.save("outputtest.png", "png")
    print(len(colorlist))

t1 = time.time()

pixel_art_check('6.7/Deltarune-poster.png')
t2 = time.time()

pixel_art_check('6.7/Undertale_Cast.png')
t3 = time.time()

#pixel_art_check('6.7/World_1-1_Super_Mario_Bros.png')

pixel_art_check('6.7/raiseupyourbat.jpg')
t4 = time.time()
print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(t1-t0, t2-t1, t3-t2, t4-t3, t4-t0))