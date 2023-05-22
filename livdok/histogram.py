import cv2
import numpy as np
from Image import *

for x in range(36):
    # Read the image
    img, gray = Image.read_image(x)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculate the histogram
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    # Find the mean value of the pixels
    mean = np.mean(hist)
    print("Mean: {}".format(mean))
    # Check if the image is underexposed, overexposed, or correctly exposed
    if mean < 100:
        print("Image is underexposed")
    elif mean > 150:
        print("Image is overexposed")
    else:
        print("Image is correctly exposed")

    # Display the histogram
    cv2.imshow("Histogram", hist)
    cv2.waitKey(0)
    cv2.destroyAllWindows()