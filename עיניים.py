import cv2
import imutils

# Load the input image and convert it to grayscale
image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\17.jpg")
# Resize the image
image = imutils.resize(image, width=min(1000, image.shape[1]))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use a Haar cascade classifier to detect the face in the image
face_cascade = cv2.CascadeClassifier('C:\\Users\\User\\anaconda3\\pkgs\\opencv-4.5.5-py310h1e0e658_2\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Iterate over the detected faces
for (x,y,w,h) in faces:
  # Extract the face region from the image
  face_region = gray[y:y+h, x:x+w]

  # Use a Haar cascade classifier to detect the eyes in the face region
  eye_cascade = cv2.CascadeClassifier('C:\\Users\\User\\anaconda3\\pkgs\\opencv-4.5.5-py310h1e0e658_2\\Library\\etc\\haarcascades\\haarcascade_eye.xml')
  eyes = eye_cascade.detectMultiScale(face_region)

  # Iterate over the detected eyes and draw a bounding box around them
  for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(image, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)

# Display the image with the detected eyes
cv2.imshow('Eyes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
