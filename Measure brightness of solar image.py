'''
Combine functions from
    1. Image_point_function_create_mask.py
    2. Image_paste
    3. Image_point_function_measure_brightness.py

To take a single RGB image and calculate amount of dark and light pixels.
'''
from PIL import Image, ImageOps

original_solar_image = 'images/2_0131.jpg' # original Solar image RGB

# 1. Image_point_function_create_mask.py


# Note: this part does not need to be done for each image.
# Once the mask has been made it can be used for every image.
mask_file = 'images/9_1700.jpg'  # no solar flares, so just a circle.

# functions which will be used for mapping
def threshold_9(p): # returns 255 for any values greater than 9. 0 otherwise.
    if p>9:
        return 255
    else:
        return 0

with Image.open(mask_file) as im_mask:
    im_mask = im_mask.convert("L")  # Greyscale
    im_mask = im_mask.point(threshold_9) # Set to white (255) any pixel values greater than 9.
    im_mask_invert = ImageOps.invert(im_mask) # Invert black and white
    #im_mask.save("images/mask.png")
    # im_mask_invert.save("images/mask_invert.png")
    #im_mask.show()
    #print(im_mask.mode)

#  2. Image_paste
'''
1. Surround original image with black.
2. Surround original image with white.
'''

infile = original_solar_image # original Solar image RGB
maskfile  = 'images/mask.png' # white circle on black background, greyscale L
with Image.open(infile) as im:
    # convert original image to greyscale so that it matches the maskfile
    im = im.convert('L')
    with Image.open(maskfile) as j_mask:
        # paste the original file onto the mask
        j_mask.paste(im, mask = j_mask)
        j_mask.show()
        j_mask.save('images/black_surround.jpg')
# this has surrounded the original image with black and saved it as black_surround


maskfile  = 'images/mask_invert.png' # black circle on white background, greyscale L
with Image.open(infile) as im:
    # convert original image to greyscale so that it matches the maskfile
    im = im.convert('L')
    with Image.open(maskfile) as j_mask:
        # paste the original file onto the mask
        im.paste(j_mask, mask = j_mask)
        im.show()
        im.save('images/white_surround.jpg')
# this has surrounded the original image with white and saved it as white_surround

#
# 3. Image_point_function_measure_brightness.py
infile_black_surround = 'images/black_surround.jpg' # Solar image greyscale with black surround
infile_white_surround = 'images/white_surround.jpg' # Solar image greyscale with white surround

# threshold for classifying pixels as 'bright'
def j_point_fn1(x):
    if x>180:
        return True
    else:
        return False

# threshold for classifying pixels as 'dark'
def j_point_fn2(x):
    if x<50:
        return True
    else:
        return False

def j_point_fn3(x):
    if x==1:
        return 0
    else:
        return 1

with Image.open(infile_black_surround) as im:
    im = im.point(j_point_fn1, mode='1')
    im.show()
    print('Number of white pixels is ', sum( list(im.getdata())))

with Image.open(infile_white_surround) as im:

    im = im.point(j_point_fn2, mode='1')
    im_invert = im.point(j_point_fn3)  # Invert black and white
    im_invert.show()
    print('Number of black pixels is ', sum( list(im.getdata())))
