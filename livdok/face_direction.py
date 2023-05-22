import cv2
import face_alignment
import math
from Image import *
# Load image
img,gry = Image.read_image(31)

# Run face alignment
fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D)
preds = fa.get_landmarks(img)

# Calculate angle between eyes
eye_angle = math.atan2(preds[0][27][1] - preds[0][32][1], preds[0][27][0] - preds[0][32][0])

# Check if face is looking left or right
if eye_angle > 0:
    print("Face is looking left")
else:
    print("Face is looking right")