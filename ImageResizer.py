#!/usr/bin/python

import sys
import PIL
from PIL import Image

def ResizeImages(ImageList, ScaleFactor):
    for i in ImageList:
        print (i)
        img = Image.open(i)
        wpercent = ScaleFactor/float(img.size[0])
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((ScaleFactor,hsize),PIL.Image.ANTIALIAS)
        img.save(i)


