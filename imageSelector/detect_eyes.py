import cv2
import face_recognition
from Image import *


def eyes(x):
    image, gray = Image.read_image(x)
    # Find all facial features in the image
    face_landmarks_list = face_recognition.face_landmarks(image)
    eyes_region = []

    # Loop through each face
    for face_landmarks in face_landmarks_list:
        # Get the coordinates of the eyes
        left_eye = face_landmarks['left_eye']
        right_eye = face_landmarks['right_eye']
        print(left_eye)
        # change the col

        # cv2.rectangle(image, ( left_eye[0][0], left_eye[1][1]), (left_eye[3][0], left_eye[5][1]), (0, 0, 255), 2)
        eyes_region.append(gray[left_eye[1][1] - 10:left_eye[5][1] + 10, left_eye[0][0] - 10:left_eye[3][0] + 10])
        eyes_region.append(gray[right_eye[1][1] - 10:right_eye[5][1] + 10, right_eye[0][0] - 10:right_eye[3][0] + 10])

        # Draw a rectangle around the eyes using OpenCV
        for (x, y) in left_eye:

            cv2.circle(image, (x, y), 2, (0, 0, 255), -1)
            # draw rectangle around the eyes
            #eyes_region.append(image[y:y + h, x:])
            #face_region.append(image[top:bottom, left:right])

            #cv2.rectangle(image, (x, y), (x + 10, y + 10), (0, 0, 255), 2)
        for (x, y) in right_eye:
            cv2.circle(image, (x, y), 2, (0, 0, 255), -1)
        cv2.imshow("Eyes", image)
        cv2.waitKey(0)
    return eyes_region
for i in range(1):
    x=eyes(26)
