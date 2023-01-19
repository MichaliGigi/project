from Image import *

for x in range(5,7):

    # Read the input image
    image, gray = Image.read_image(x)

    # Apply a Gaussian blur
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Compute the Canny edge map
    edges = cv2.Canny(gray, 50, 100)

    # Display the result
    cv2.imshow('edges', edges)
    cv2.waitKey()
