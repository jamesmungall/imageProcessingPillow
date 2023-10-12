# https://www.geeksforgeeks.org/python-pil-image-point-method/
# Image.point() Maps this image through a lookup table or function.
'''
I am going to use this function to create a mask image. This image will be a circle
 made from the circular image of the sun, 9_1700.jpg.

The output file is mask.png. This is a greyscale image (mode is L).

'''
from PIL import Image
mask_file = '9_1700.jpg' # no solar flares, so just a circle.

# functions which will be used for mapping
def threshold_9(p): # returns 255 for any values greater than 9. 0 otherwise.
    if p>9:
        return 255
    else:
        return 0

def multiply_pixels(p): # Not currently used, but this brightens whole image.
    return p*10

with Image.open(mask_file) as im_mask:
    im_mask = im_mask.convert("L")  # Greyscale
    im_mask = im_mask.point(threshold_9) # Set to white (255) any pixel values greater than 9.

    #im_mask.save("mask.png")
    #im_mask.show()
    #print(im_mask.mode)