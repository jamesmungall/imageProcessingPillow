# https://www.geeksforgeeks.org/python-pil-image-point-method/
# Image.point() Maps this image through a lookup table or function.

from PIL import Image
mask_file = '9_1700.jpg' # no solar flares, so just a circle.
infile = '2_0131.jpg'

# functions which will be used for mapping
def threshold_9(p):
    if p>9:
        return 255
    else:
        return 0

def multiply_pixels(p):
    return p*10

with Image.open(mask_file) as im_mask:
    im_mask = im_mask.convert("L")  # Greyscale
    im_mask = im_mask.point(threshold_9) # Set to white (255) any pixel values greater than 9.
    im_mask.save("mask.png")
    #im_mask.show()
    #print(im_mask.mode)