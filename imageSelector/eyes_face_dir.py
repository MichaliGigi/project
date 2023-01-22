import cv2
import face_alignment
from Image import *

img,x = Image.read_image(31)

# Load image
#img = cv2.imread("path/to/image.jpg")

# Run face alignment
preds = face_alignment.get_landmarks(img)


# Extract the x and y coordinates of the left and right eye
left_eye_x = (preds[0][36][0] + preds[0][39][0]) / 2
left_eye_y = (preds[0][36][1] + preds[0][39][1]) / 2
right_eye_x = (preds[0][42][0] + preds[0][45][0]) / 2
right_eye_y = (preds[0][42][1] + preds[0][45][1]) / 2

# Calculate the distance between the eyes
eye_distance = ((left_eye_x - right_eye_x) ** 2 + (left_eye_y - right_eye_y) ** 2) ** 0.5

# Check if the eyes are closed
if eye_distance < 20:
    print("Eyes are closed")
else:
    print("Eyes are open")
