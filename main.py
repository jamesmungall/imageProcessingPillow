# https://realpython.com/image-processing-with-the-python-pillow-library/

from PIL import Image


def j_load(filename):
    with Image.open(filename) as img: img.load()
    # You call the open() function to read the image from the file and .load() to read the image into memory so that
    # the file can now be closed. You use a with statement to create a context manager to ensure the file is closed
    # as soon as it’s no longer needed.
    return img


def j_save():
    img = j_load("buildings.jpg")
    img.thumbnail((200, 200))
    img.save("thumb.jpg")


def j_crop():
    img = j_load("buildings.jpg")
    cropped_img = img.crop((300, 150, 700, 1000))
    cropped_img.show()


def j_resize():
    img = j_load("buildings.jpg")
    resized_img = img.resize((img.width // 4, img.height // 4))
    # double brackets because dimensions must be a tuple. // 4 divides by 4 without giving a remainder or decimal.
    resized_img.show()


def j_reduce():
    img = j_load("buildings.jpg")
    # reduces image size by a scale factor of 4
    reduced_img = img.reduce(4)
    reduced_img.show()


def j_thumbnail():
    img = j_load("buildings.jpg")
    # sets image to a maximum size that you set
    img.thumbnail((200, 200))
    # actually alters img
    img.show()


def j_transpose():
    img = j_load("buildings.jpg")
    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.show()


def j_rotate():
    img = j_load("buildings.jpg")
    rotated_img = img.rotate(45, expand=True)
    rotated_img.show()


def j_convert():
    img = j_load("buildings.jpg")
    gray_img = img.convert("L")  # Greyscale
    gray_img.show()


def j_split():
    img = j_load("buildings.jpg")
    red, green, blue = img.split()
    red.show()
    # Note that this is a greyscale image (type "L")


def j_merge():
    img = j_load("buildings.jpg")
    red, green, blue = img.split()
    # put a zero at each point in the zeroed band. 'i' is a dummy variable.
    zeroed_band = red.point(lambda i: 0)
    red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
    green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
    blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))
    rgb_images = (red_merge, green_merge, blue_merge)
    for i in rgb_images:
        i.show()
