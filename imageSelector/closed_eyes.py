import cv2
import face_recognition
from Image import *


image,g=Image.read_image(36)
# Find all facial features in the image
face_landmarks_list = face_recognition.face_landmarks(image)

# Loop through each face
for face_landmarks in face_landmarks_list:
    # Get the coordinates of the eyes
    left_eye = face_landmarks['left_eye']
    right_eye = face_landmarks['right_eye']

 # Get the ratio of the eyelid to the eye for each eye
    left_eye_ratio = (left_eye[5][1] - left_eye[1][1]) / (left_eye[3][1] - left_eye[1][1])
    right_eye_ratio = (right_eye[5][1] - right_eye[1][1]) / (right_eye[3][1] - right_eye[1][1])

    # Check if the ratio is below a certain threshold
    if left_eye_ratio < 0.25 and right_eye_ratio < 0.25:
        print("Eyes are closed.")
    else:
        print("Eyes are open.")
# Show the image
cv2.imshow("cloEyes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()