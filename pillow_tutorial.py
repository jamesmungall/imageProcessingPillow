# ref: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html


# Take the value of each pixel and multiply by 10.
from PIL import Image
infile = '2_0131.jpg'

with Image.open(infile) as im:
    out = im.point(lambda i: i * 10)
#out.show()

# create a mask
infile = '9_1700.jpg'

with Image.open(infile) as im:
    # select regions where pixel value is less than 100
    mask = im.point(lambda i: i < 100 and 255)

mask.show()

