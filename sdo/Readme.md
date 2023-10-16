### SDO analysis  

1. Get latest images, e.g. https://sdo.gsfc.nasa.gov/assets/img/latest/latest_512_1700.jpg

Function to to this is  in sdo_image_from_url.py  
Within this file, the function urllib.request.urlretrieve actually makes the request.  

2. Create mask and add as an alpha channel to each image.

Functions are in sdo_mask.py  
A black and white image is generated to create the mask.  
Then this is used in the function Image.putalpha  

3. Count frequencies of dark and light pixels

Function is in sdo_analyse.py  
Image is pre-multiplied by alpha by setting mode to RGBa.  
Then pixels are summed according to value.  

