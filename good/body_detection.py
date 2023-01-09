from Image import *

# Load the cascade
body_cascade = cv2.CascadeClassifier('C:\\Users\\User\\anaconda3\\pkgs\\opencv-4.5.5-py310h1e0e658_2\\Library\\etc\\haarcascades\\haarcascade_fullbody.xml')

for x in range(22):

    image,gray=Image.read_image(x)

    # Detect bodies

    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw a rectangle around the bodies
    for (x, y, w, h) in bodies:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the output
    cv2.imshow('image', image)
    cv2.waitKey()
