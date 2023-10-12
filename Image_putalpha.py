# https://note.nkmk.me/en/python-pillow-putalpha/

from PIL import Image
from PIL import ImageDraw

infile = '3_0171.jpg'

with Image.open(infile) as im:
    im.putalpha(255) # alpha set to 100% transparent
    #im.show()
    #print(im.mode)

    # You can use an image as the alpha layer.
    # Draw a white circle on a black background
    im_a = Image.new("L", im.size, 0)
    draw = ImageDraw.Draw(im_a)
    draw.ellipse((0, 0, 512, 512), fill=255)
    im.putalpha(im_a)
    im.show()



