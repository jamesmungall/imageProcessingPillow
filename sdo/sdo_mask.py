from PIL import Image

# the Solar image to have the alpha channel added.
#original_filename = 'images/latest/latest_512_0131.jpg'

# the alpha channel to be added
def j_make_mask(mask_file = '../images/latest/latest_512_1700.jpg'):
    # create mask file from the 1700A image with no solar flares, so just a circle.

    with Image.open(mask_file) as im_mask:
        im_mask = im_mask.convert("L")  # Greyscale
        im_mask = im_mask.point(lambda x:x>9 and 255 or 0)  # Set to white (255) any pixel values greater than 9.
        im_mask.save('../images/mask.png')

def j_mask_fn(original_filename, mask_filename, save_filename):

    with Image.open(original_filename) as im:
        with Image.open(mask_filename) as im_mask:
            if im_mask.mode != "L":
                im_mask = im_mask.convert("L")
            im.putalpha(im_mask)
            im.show()
            im.save(save_filename)


