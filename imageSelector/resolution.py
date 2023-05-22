# import the necessary packages

from Image import *
for x in range(27):
    # Read the image file
    image,gray = Image.read_image(x)

    # Get the width and height of the image
    height, width = image.shape[:2]

    # Print the resolution
    print(f'The resolution of the image is {width}x{height}')
