import cv2
import imutils
from imutils.object_detection import non_max_suppression
import numpy as np
"""
# Load the input image
image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\4.jpg")

# Load the Haar cascade classifier for detecting faces
face_cascade = cv2.CascadeClassifier('C:\\Users\\User\\anaconda3\\pkgs\\opencv-4.5.5-py310h1e0e658_2\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

# Resize the image
image = imutils.resize(image, width=min(1000, image.shape[1]))
# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Iterate over the detected faces
for (x,y,w,h) in faces:
  # Extract the face region from the image
  face_region = gray[y:y+h, x:x+w]

  # Use a Haar cascade classifier to detect the eyes in the face region
  eye_cascade = cv2.CascadeClassifier('C:\\Users\\User\\anaconda3\\pkgs\\opencv-4.5.5-py310h1e0e658_2\\Library\\etc\\haarcascades\\haarcascade_eye.xml')

  eyes = eye_cascade.detectMultiScale(face_region)

  # Iterate over the detected eyes
  for (ex,ey,ew,eh) in eyes:
    # Extract the eye region from the face region
    eye_region = face_region[ey:ey+eh, ex:ex+ew]
    #cv2.rectangle(face_region, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Save the output image
    cv2.imshow("After NMS", eye_region)



    # Check if the eye is closed by measuring the amount of black pixels in the eye region
    #total_pixels = ew * eh
    #black_pixels = cv2.countNonZero(eye_region)
    #if black_pixels / total_pixels > 0.5:
     # print("Closed eye detected")

cv2.waitKey(0)"""

import cv2

# Load the input image and convert it to grayscale
image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\4.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use a deep learning-based face detection model to detect the face in the image
face_detector = cv2.dnn.readNetFromCaffe('face_detector.prototxt', 'face_detector.caffemodel')
(h, w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
face_detector.setInput(blob)
detections = face_detector.forward()

# Iterate over the detected faces
for i in range(detections.shape[2]):
  confidence = detections[0, 0, i, 2]

  # Only consider detections with a high confidence level
  if confidence > 0.5:
    # Compute the bounding box of the face
    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
    (startX, startY, endX, endY) = box.astype("int")

    # Extract the face region from the image
    face_region = image[startY:endY, startX:endX]

    # Use a deep learning-based eye detection model to detect the eyes in the face region
    eye_detector = cv2.dnn.readNetFromCaffe('eye_detector.prototxt', 'eye_detector.caffemodel')
    blob = cv2.dnn.blobFromImage(face_region, 1.0, (300, 300), (104.0, 177.0, 123.0))
    eye_detector.setInput(blob)
    eye_detections = eye_detector.forward()

    # Iterate over the detected eyes
    for j in range(eye_detections.shape[2]):
      confidence = eye_detections[0, 0, j, 2]

      # Only consider detections with a high confidence level
      if confidence > 0.5:
        # Compute the bounding box of the eye
        box = eye_detections[0, 0, j, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        # Extract the eye region from the face region
        eye_region = face_region[startY:endY, startX:endX]

        # Check if the eye is closed by measuring the amount of black pixels in the eye region
        total_pixels = (endX - startX) * (endY - startY)
        black_pixels = cv2.countNonZero(eye_region)
        if black_pixels / total_pixels> 0.5:
           print("Closed eye detected")
