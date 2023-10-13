from PIL import Image

import sdo_mask
import sdo_analyse
import sdo_image_from_url
'''
1. Get latest images, e.g. https://sdo.gsfc.nasa.gov/assets/img/latest/latest_512_1700.jpg
'''
# Save to images/ folder  with filenames
# 'latest_' + resolution + '_' + wavelength + '.jpg' e.g.latest_512_0211.jpg

online_folder = 'https://sdo.gsfc.nasa.gov/assets/img/latest/'
resolution = '256' # options are 170 (about 8KB), 256, 512, 1024, 2048, 3072, 4096 (about 8MB)
wavelengths = ['0094', '0131', '0171', '0193', '0211', '0304', '0335', '1600', '1700']
my_urls = []
local_folder = 'images/'
local_files = []
for wavelength in wavelengths:
    local_files.append('latest_' + resolution + '_' + wavelength + '.jpg')
for filename in local_files:
    my_urls.append(online_folder + filename)


# COMMENT LINE BELOW TO PREVENT FROM RUNNING
sdo_image_from_url.j_sdo_image_from_url(urls= my_urls, save_folder =local_folder, save_filenames  = local_files)

'''
2. Create mask and add as an alpha channel to each image.
'''
# Create mask image using the 1700 wavelength since it has no solar flares.
# This will have been the last file downloaded.
# Note; this mask image may need tidying up in gimp.

# COMMENT LINE BELOW TO PREVENT FROM RUNNING
sdo_mask.j_make_mask(mask_template_file =local_folder+local_files[-1], savemask_folder_file = local_folder + 'mask.png')


# the Solar image to have the alpha channel added.

# the alpha channel to be added
mask_filename = local_folder + 'mask.png'
images_with_alpha = []
for filename in local_files:
    original = local_folder + filename

    # image with alpha added
    image_with_alpha = original[:-4] + '_masked.png'
    images_with_alpha.append(image_with_alpha)
    #print('mask added to ' + original + ' to create ' + image_with_alpha)
    sdo_mask.j_mask_fn(original, mask_filename, image_with_alpha)

'''
3. Count frequencies of dark and light pixels
'''
for file in images_with_alpha:
    #print('Counting frequencies for ' + file)
    # Count frequency of dark and light pixels.
    sdo_analyse.j_sdo_analyse(file)
