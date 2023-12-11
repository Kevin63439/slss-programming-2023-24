# Images and Python
# Author: Kevin Wong
# 11 December 2023

from PIL import Image

# Recall that we can open up files in Python
with Image.open("./Images/kid-green.jpg") as im:
    # get pixel information
    pixel = im.getpixel((0, 0))

    # print the pixel info
    print(pixel)

    # get the middle pixel
    middle = im.width