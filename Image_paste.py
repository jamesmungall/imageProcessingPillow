

from PIL import Image

'''
1. Surround original image with black.
2. Surround original image with white.
'''

infile = 'images/3_0171.jpg' # original Solar image RGB
maskfile  = 'images/mask.png' # white circle on black background, greyscale L
with Image.open(infile) as im:
    # convert original image to greyscale so that it matches the maskfile
    im = im.convert('L')
    with Image.open(maskfile) as j_mask:
        # paste the original file onto the mask
        j_mask.paste(im, mask = j_mask)
        j_mask.show()
        j_mask.save('images/3_0171_black_surround.jpg')


maskfile  = 'images/mask_invert.png' # black circle on white background, greyscale L
with Image.open(infile) as im:
    # convert original image to greyscale so that it matches the maskfile
    im = im.convert('L')
    with Image.open(maskfile) as j_mask:
        # paste the original file onto the mask
        im.paste(j_mask, mask = j_mask)
        im.show()
        im.save('images/3_0171_white_surround.jpg')
