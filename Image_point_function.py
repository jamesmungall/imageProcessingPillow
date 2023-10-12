# https://www.geeksforgeeks.org/python-pil-image-point-method/
# Image.point() Maps this image through a lookup table or function.

from PIL import Image
infile = '2_0131.jpg'

# functions which will be used for mapping
def threshold_pixels(p):
    if p>91:
        return 255
    else:
        return 0

def multiply_pixels(p):
    return p*10

with Image.open(infile) as im:
    out = im.point(threshold_pixels)
    #out.show()
    out = im.point(multiply_pixels)
    #out.show()