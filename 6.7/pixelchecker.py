from PIL import Image
import time

t0 = time.time()

uniquecolors = []
pixelart = []
pixelartlen = []
brushart = []
brushartlen = []

def pixel_art_check(imgname):
    inp_img = Image.open(imgname)
    pixels = inp_img.getdata()
    uniquecolors = set(pixels)
    print(len(uniquecolors))

def list_append(imgname, pixcount):
    if len(uniquecolors) <= 114500:
        pixelart.append(imgname)
        pixelartlen.append(pixcount)
    else:
        brushart.append(imgname)
        brushartlen.append(pixcount)

#------------------------------------------------------------------------
t1 = time.time()

pixel_art_check('6.7/Deltarune-poster.png')
list_append('6.7/Deltarune-poster.png', len(uniquecolors))
uniquecolors = []
t2 = time.time()

pixel_art_check('6.7/Undertale_Cast.png')
list_append('6.7/Undertale_Cast.png', len(uniquecolors))
uniquecolors = []
t3 = time.time()

pixel_art_check('6.7/raiseupyourbat.jpg')
list_append('6.7/raiseupyourbat.jpg', len(uniquecolors))
t4 = time.time()

pixel_art_check('6.7/hatsune-miku.jpg')
list_append('6.7/hatsune-miku.jpg', len(uniquecolors))
t5 = time.time()

pixel_art_check('6.7/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg')
list_append('6.7/Mona_Lisa,_by_Leonardo_da_Vinci,_from_C2RMF_retouched.jpg', len(uniquecolors))
t6 = time.time()

print(pixelart)
print(brushart)
print(pixelartlen)
print(brushartlen)
print('Loading the functions and modules took {:.2f} seconds. The first image took {:.2f} seconds, the second image took {:.2f} seconds, the third image took {:.2f} seconds,'.format(t1-t0, t2-t1, t3-t2, t4-t3,))
print('the fourth image took {:.2f} seconds, the fifth image took {:.2f} seconds'.format(t5-t4, t6-t5))