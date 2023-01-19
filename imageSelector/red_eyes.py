import cv2
import face_recognition
from Image import *

for x in range(26):

    image,gray=Image.read_image(x)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_recognition.face_locations(gray)

    # Iterate over each face
    for (x, y, w, h) in faces:
        # Crop the face
        face = gray[y:y+h, x:x+w]

        # Detect red eyes in the face
        eyes = cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml").detectMultiScale(face)

        # Iterate over each eye
        for (ex, ey, ew, eh) in eyes:
            # Draw a rectangle around the red eye
            cv2.rectangle(image, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 0, 255), 2)

    # Show the image with red eyes detected
    cv2.imshow("Red Eyes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()