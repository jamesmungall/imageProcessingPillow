from PIL import Image, ImageOps

infile_black_surround = 'images/3_0171_black_surround.jpg' # Solar image greyscale with black surround
infile_white_surround = 'images/3_0171_white_surround.jpg' # Solar image greyscale with white surround

def j_point_fn1(x):
    if x>179:
        return True
    else:
        return False

def j_point_fn2(x):
    if x<19:
        return True
    else:
        return False

def j_point_fn3(x):
    if x==1:
        return 0
    else:
        return 1

with Image.open(infile_black_surround) as im:

    im = im.point(j_point_fn1, mode='1')
    im.show()
    print(im.mode)
    print('Number of white pixels is ', sum( list(im.getdata())))

with Image.open(infile_white_surround) as im:

    im = im.point(j_point_fn2, mode='1')
    im_invert = im.point(j_point_fn3)  # Invert black and white
    #im.show()
    im_invert.show()
    print(im.mode)
    print('Number of black pixels is ', sum( list(im.getdata())))
