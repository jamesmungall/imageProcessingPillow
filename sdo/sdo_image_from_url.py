# Opens a series of solar images from nasa url
import urllib.request

def j_sdo_image_from_url(urls, save_folder, save_filenames):

    for i in range(len(urls)):

        # Images stored in save folder as save_filenames
        urllib.request.urlretrieve(urls[i], save_folder + save_filenames[i])
        print(urls[i] + ' saved to ' + save_folder + save_filenames[i])
