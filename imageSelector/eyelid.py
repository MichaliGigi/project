import face_recognition
from shapely.geometry import Polygon
from Image import *

# Load the image
image,x = Image.read_image(31)
cv2.imshow("image", image)
cv2.waitKey(0)
# Find the facial landmarks in the image
face_landmarks_list = face_recognition.face_landmarks(image)

# Iterate over the facial landmarks
for face_landmarks in face_landmarks_list:
    # Extract the eyelid points
    left_eyelid = face_landmarks['left_eyelid']
    right_eyelid = face_landmarks['right_eyelid']

    # Create a polygon for the eyelid
    left_eyelid_poly = Polygon(left_eyelid)
    right_eyelid_poly = Polygon(right_eyelid)

    # Create a polygon for the eye
    left_eye_poly = Polygon(face_landmarks['left_eye'])
    right_eye_poly = Polygon(face_landmarks['right_eye'])

    # Calculate the ratio of eyelid area to eye area
    left_ratio = left_eyelid_poly.area / left_eye_poly.area
    right_ratio = right_eyelid_poly.area / right_eye_poly.area

    # Set the threshold
    threshold = 0.5

    # Check if the eye is open or closed
    if left_ratio < threshold:
        print("Left eye is open")
    else:
        print("Left eye is closed")

    if right_ratio < threshold:
        print("Right eye is open")
    else:
        print("Right eye is closed")