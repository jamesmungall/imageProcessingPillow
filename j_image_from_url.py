# Opens a series of solar images from nasa url
import urllib.request

filenames = ['latest/latest_512_0094.jpg',
             'latest/latest_512_0131.jpg',
             'latest/latest_512_0171.jpg',
             'latest/latest_512_0193.jpg',
             'latest/latest_512_0211.jpg',
             'latest/latest_512_0304.jpg',
             'latest/latest_512_0335.jpg',
             'latest/latest_512_1600.jpg',
             'latest/latest_512_1700.jpg']
for filename in filenames:
    my_url = "https://sdo.gsfc.nasa.gov/assets/img/"+filename
    # images stored in images folder with the same filename
    urllib.request.urlretrieve(my_url, "images/" + filename)