import cv2
import face_recognition

from Image import *
def faces(x):
    image,gray=Image.read_image(x)
    # Find all the faces in the image
    face_locations = face_recognition.face_locations(image)
    face_region=[]
    # Loop through each face
    for (top, right, bottom, left) in face_locations:
        # Draw a rectangle around the face using OpenCV
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        face_region.append(image[top:bottom,left:right])

    #cv2.imshow("face", image)
    #cv2.waitKey(0)

    return face_region,face_locations

