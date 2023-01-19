# import the necessary packages
from Libraries import *
for x in range(21):
    # Read the image file
    image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\{}.jpg".format(x))

    # Get the width and height of the image
    height, width = image.shape[:2]

    # Print the resolution
    print(f'The resolution of the image is {width}x{height}')
