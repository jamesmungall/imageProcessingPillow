from PIL import Image

import sdo_mask
import sdo_analyse
import sdo_image_from_url

# get latest images
sdo_image_from_url.j_sdo_image_from_url()

# create mask image
sdo_mask.j_make_mask()


# the Solar image to have the alpha channel added.
original_filename = '../images/latest/latest_512_1700.jpg'

# the alpha channel to be added
mask_filename = '../images/mask.png'

# image with alpha added
image_with_alpha = original_filename[:-4] + '_masked.png'

sdo_mask.j_mask_fn(original_filename, mask_filename, image_with_alpha)
sdo_analyse.j_sdo_analyse(image_with_alpha)