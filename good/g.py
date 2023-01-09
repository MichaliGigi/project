import cv2

# Load the image
image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\4.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use a Haar cascade classifier to detect faces
face_cascade = cv2.CascadeClassifier("C:\\Users\\User\\anaconda3\\pkgs\\opencv-4.5.5-py310h1e0e658_2\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Iterate over the faces and draw a rectangle around each one
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Save the image with the rectangles
cv2.imwrite("image_with_rectangles.jpg", image)
