from Image import *

for x in range(27):

    # Read the input image
    image, gray = Image.read_image(x)

    # Apply a Gaussian blur
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Compute the Canny edge map
    edges = cv2.Canny(gray, 50, 100)

    # Find contours in the edges
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    cv2.imshow("After", edges)
    cv2.waitKey(0)
