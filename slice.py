from PIL import Image

from main import j_load


def j_slice(filename: str, number_of_slices: int, vertical_slices: bool):
    print("hello from j_slice")
    img = j_load(filename)
    if isinstance(img, Image.Image):
        print("File", filename, "opened successfully.")
        print(img)

    slices = []
    if vertical_slices:
        width = img.width // number_of_slices
        for i in range(number_of_slices):
            single_slice = img.crop((width * i, 0, width * (i + 1), img.height))
            slices.append(single_slice)
    else:
        height = img.height // number_of_slices
        for i in range(number_of_slices):
            single_slice = img.crop((0, height * i, img.width, height * (i + 1)))
            slices.append(single_slice)
    return slices


def test_slice():
    slices = j_slice(filename="buildings.jpg", number_of_slices=3, vertical_slices=True)
    for img in slices:
        img.show()


test_slice()
