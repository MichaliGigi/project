# מזהה מקסים!!
# import the necessary packages
from Image import *


for x in range(26):
    image,gray=Image.read_image(x)

    # Compute the gradient magnitude and direction using the Sobel operator
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    direction = np.arctan2(sobel_y, sobel_x)

    # Normalize the gradient magnitude to [0, 255]
    min_val, max_val, _, _ = cv2.minMaxLoc(magnitude)
    magnitude = (magnitude - min_val) / (max_val - min_val) * 255
    magnitude = magnitude.astype(np.uint8)

    # Threshold the gradient magnitude to create a binary image
    _, binary = cv2.threshold(magnitude, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the output image
    cv2.imshow("After", binary)
    cv2.waitKey(0)
