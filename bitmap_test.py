import sys
import os
from bitmap_file import *

path = sys.argv[0].rsplit('/', 1)[0]
newfolder = path+"/test_output"
if not os.path.exists(newfolder):
    os.makedirs(newfolder)

# Black 1x1px bmp file
black = bytearray(6)
BmpFile(black, 1, 1, 'test_output/black.bmp').write()

# White 1x1px bmp file
white = bytearray([255, 255, 255, 0, 0, 0])
BmpFile(white, 1, 1, 'test_output/white.bmp').write()

# Red 1x1px bmp file
red = bytearray([0, 0, 255, 0, 0, 0])
BmpFile(red, 1, 1, 'test_output/red.bmp').write()

# Green 1x1px bmp file
green = bytearray([0, 255, 0, 0, 0, 0])
BmpFile(green, 1, 1, 'test_output/green.bmp').write()

# Blue 1x1px bmp file
blue = bytearray([255, 0, 0, 0, 0, 0])
BmpFile(blue, 1, 1, 'test_output/blue.bmp').write()

# 6x4px french flag file
hexblue = bytearray.fromhex('FF0000')
hexwhite = bytearray.fromhex('FFFFFF')
hexred = bytearray.fromhex('0000FF')
height = 4
width = 6
flagdata = bytearray()
for h in range(height):
    for w in range(width + ((width * 3) % 4)):
        if w < 2:
            flagdata.extend(hexblue)
        elif w < 4:
            flagdata.extend(hexwhite)
        elif w < 6:
            flagdata.extend(hexred)
        else:
            flagdata.extend(bytearray(1))
BmpFile(flagdata, width, height, 'test_output/flag.bmp').write()
