import cv2
import face_recognition
import numpy as np

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

        eyes_region.append(image[left_eye[1][1] :left_eye[5][1] , left_eye[1][0] :left_eye[2][0] ])
        eyes_region.append( image[right_eye[1][1] :right_eye[5][1], right_eye[1][0] :right_eye[2][0] ])

    for pic in eyes_region:
        b,r,g=cv2.split(pic)
        if np.greater(r,b).any() and np.greater(r,g).any():
            print(x,"red")

        #else:
          #  print("not red")
for i in range(35):
    x=eyes(i)
