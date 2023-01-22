import cv2
import face_recognition
from Image import *


def eyes(x):
    print(x)
    image, gray = Image.read_image(x)
    # Find all facial features in the image
    face_landmarks_list = face_recognition.face_landmarks(image)
    eyes_region = []

    # Loop through each face
    for face_landmarks in face_landmarks_list:
        # Get the coordinates of the eyes
        left_eye = face_landmarks['left_eye']
        right_eye = face_landmarks['right_eye']
        left_eyebrow = face_landmarks['left_eyebrow']
        right_eyebrow = face_landmarks['right_eyebrow']



        y_max_eyebrow=max([coordinate[1] for coordinate in left_eyebrow])


        x_max = max([coordinate[0] for coordinate in left_eye])
        x_min = min([coordinate[0] for coordinate in left_eye])
        #y_max = max([coordinate[1] for coordinate in left_eye])
        #y_min = min([coordinate[1] for coordinate in left_eye])
        y_max = left_eye[5][1]
        y_min = left_eye[1][1]
        # establish the range of x and y coordinates
        x_range = x_max - x_min
        y_range = y_max - y_min
        print("range",x_range/ y_range,"y",y_range)

        if (y_range)<=4 and (x_range/y_range)>=3:
            print("left eye is closed")
        else:
            print("left eye is open")
for i in range(1):
    eyes(9)






#meatzben beramottttttttttttttttttttttttttttttttttttttttttttttttttt!!
