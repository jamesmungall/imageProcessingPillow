from PIL import Image

filename= '../images/latest/latest_512_0094_masked.png'


'''
Count number of pixels with a value >200 and alpha = 255.
Having pre-multiplied by alpha, all pixels will have a value
 of 0 where alpha was 0.
It is useful to know how many black and white pixels there are in the alpha
channel. This tells us how many 0s are due to the masking.
'''

def j_sdo_analyse(filename):
    def n_below(threshold, single_band):
        return sum(list(single_band.
                        # return 1 if x>200, 0 otherwise
                        point(lambda x: x < threshold and 1 or 0).
                        getdata()))

    def n_above(threshold, single_band):
        return sum(list(single_band.
                        # return 1 if x>200, 0 otherwise
                        point(lambda x: x > threshold and 1 or 0).
                        getdata()))

    def make_dicts(band, n_alpha):
        return {
            'total': n_alpha['white'],
            'full_on': n_above(254, band),
            'full_off': n_below(1, band) - n_alpha['black'],
            'above 200': n_above(200, band),
            'below 55': n_below(55, band) - n_alpha['black']
        }

    with Image.open(filename) as im:
        # pre-multiply by alpha. All RGB pixels set to 0 where alpha is zero.
        im = im.convert("RGBa")
        #im.show()
        red, green, blue, alpha = im.split()
        im_greyscale = im.convert("L")

        n_alpha = {
            'total':alpha.height * alpha.width,
            'white':n_above(254, alpha), # number of full white (255) pixels.
            'black':n_below(1, alpha)
       }

        #print('n_alpha', n_alpha)
        print(filename, make_dicts(im_greyscale, n_alpha))

#j_sdo_analyse(original_filename)
