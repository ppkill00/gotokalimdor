import numpy
from PIL import Image

here = Image.open(r"target2.png")
big  = Image.open(r"source3.png")

herear = numpy.asarray(here)
bigar  = numpy.asarray(big)

hereary, herearx = herear.shape[:2]
bigary,  bigarx  = bigar.shape[:2]

stopx = bigarx - herearx + 1
stopy = bigary - hereary + 1

for x in range(0, stopx):
    for y in range(0, stopy):
        x2 = x + herearx
        y2 = y + hereary
        pic = bigar[y:y2, x:x2]
        test = (pic == herear)
        if test.all():
            print(x,y)