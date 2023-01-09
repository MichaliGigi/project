#מזהה גבולות אבל לא הכי מדויק
#פחות טוב מ"זיהוי קצוות3"
import cv2
import numpy as np
for x in range(21):
    # Load the input image
    image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\{}.jpg".format(x))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Compute the Laplacian of the image
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)

    # Normalize the Laplacian to [0, 255]
    min_val, max_val, _, _ = cv2.minMaxLoc(laplacian)
    laplacian = (laplacian - min_val) / (max_val - min_val) * 255
    laplacian = laplacian.astype(np.uint8)

    # Threshold the Laplacian to create a binary image
    _, binary = cv2.threshold(laplacian, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the output image
    cv2.imshow("After NMS", binary)
    cv2.waitKey(0)