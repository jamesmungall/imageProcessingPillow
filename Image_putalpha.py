# https://note.nkmk.me/en/python-pillow-putalpha/
'''
An alpha channel is added to the solar image using the 'mask.png' greyscale image
 created using the Image.point function.

'''
from PIL import Image

infile = 'images/3_0171.jpg' # the Solar image to have the alpha channel added.

with Image.open(infile) as im:
    # You can use an image as the alpha layer.
    with Image.open('images/mask.png') as im_mask:
        im.putalpha(im_mask)
        im.show()



