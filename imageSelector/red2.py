import cv2
import face_recognition
from Image import *

for x in range(22):

    image,gray=Image.read_image(x)
    # Find all facial features in the image
    face_landmarks_list = face_recognition.face_landmarks(image)

    # Loop through each face
    for face_landmarks in face_landmarks_list:
        # Get the coordinates of the eyes
        left_eye = face_landmarks['left_eye']
        right_eye = face_landmarks['right_eye']

        # Draw a rectangle around the eyes using OpenCV
        for (x, y) in left_eye:
            cv2.circle(image, (x, y), 2, (0, 0, 255), -1)
        for (x, y) in right_eye:
            cv2.circle(image, (x, y), 2, (0, 0, 255), -1)

    # Show the image
    cv2.imshow("Eyes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


for (ex, ey, ew, eh) in eyes:
        eye_roi = roi_gray[ey:ey+eh, ex:ex+ew]
        threshold = cv2.getTrackbarPos("threshold", "eye")
        _, eye_thresh = cv2.threshold(eye_roi, threshold, 255, cv2.THRESH_BINARY)
        if cv2.countNonZero(eye_thresh) < (ew*eh)/5:
            print("Closed Eye detected at coordinates: (x, y) = ({}, {})".format(x+ex, y+ey))