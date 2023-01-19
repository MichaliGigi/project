from Image import *


# Load the Haar cascade classifiers for lower and upper body
lower_body_cascade = cv2.CascadeClassifier('C:\\Users\\User\\anaconda3\\pkgs\\opencv-4.5.5-py310h1e0e658_2\\Library\\etc\\haarcascades\\haarcascade_lowerbody.xml')
upper_body_cascade = cv2.CascadeClassifier('C:\\Users\\User\\anaconda3\\pkgs\\opencv-4.5.5-py310h1e0e658_2\\Library\\etc\\haarcascades\\haarcascade_upperbody.xml')

for x in range(22):

    image,gray=Image.read_image(x)

    # Detect the lower body
    lower_bodies = lower_body_cascade.detectMultiScale(gray, 1.2, 3)

    # Draw a rectangle around the lower body
    for (x, y, w, h) in lower_bodies:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Detect the upper body
    upper_bodies = upper_body_cascade.detectMultiScale(gray, 1.1, 3)

    # Draw a rectangle around the upper body
    for (x, y, w, h) in upper_bodies:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the output image
    cv2.imshow('Image', image)
    cv2.waitKey(0)