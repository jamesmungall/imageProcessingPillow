from PIL import Image

# the Solar image to have the alpha channel added.
#original_filename = 'images/latest/latest_512_0131.jpg'

# Make black and white image which will be used
# as the alpha channel to be added.
def j_make_mask(mask_template_file ='../images/latest/1700.jpg', savemask_folder_file = '../images/mask.png'):
    # create mask file from the 1700A image since it has no solar flares.

    with Image.open(mask_template_file) as im_mask:
        im_mask = im_mask.convert("L")  # Greyscale
        # Make the sun fully white.
        im_mask = im_mask.point(lambda x:x>9 and 255 or 0)  # Set to white (255) any pixel values greater than 9.
        im_mask.save(savemask_folder_file)
        print(mask_template_file + ' used to create ' + savemask_folder_file)

def j_mask_fn(original_filename, mask_filename, save_filename):

    with Image.open(original_filename) as im:
        with Image.open(mask_filename) as im_mask:
            if im_mask.mode != "L":
                im_mask = im_mask.convert("L")
            im.putalpha(im_mask)
            im.save(save_filename)


