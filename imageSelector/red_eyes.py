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
        b,g,r=cv2.split(pic)
        tolerance = 50
        counter = 0
        num_of_red=10
        # iterate through all pixels in the image
        for i in range(r.shape[0]):
            for j in range(r.shape[1]):
                # get the RGB values of the current pixel
                red, green, blue = r[i][j], g[i][j], b[i][j]
                if red > green + tolerance and red > blue + tolerance:
                    counter += 1
        if counter > num_of_red:
            print("A red eye was found!")

for i in range(37):
    print(i)
    eyes(i)


