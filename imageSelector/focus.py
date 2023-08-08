#להוסיף בדיקה על אוביקט ראשי
# import the necessary packages
from Image import *

threshold=750
for x in range(42,44):

    # Load the image and convert it to grayscale
    image,gray = Image.read_image(x)

    # Find the gradient magnitude and direction of the image
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    magnitude, direction = cv2.cartToPolar(sobelx, sobely, angleInDegrees=True)

    # Calculate the focus measure using the gradient magnitude
    focus_measure = cv2.Laplacian(magnitude, cv2.CV_64F).var()
    print("Focus measure: {}".format(focus_measure))
    # Determine if the image is in focus
    if focus_measure > threshold:
        print("The image is in focus")
    else:
        print("The image is not in focus")

    cv2.imshow("f", image)
    cv2.waitKey(0)