#מזהה יפה, לפעמים יש זיהויים כוזבים
# import the necessary packages
from Image import *

# Load the Haar cascade classifier for detecting faces
face_cascade = cv2.CascadeClassifier('C:\\Users\\User\\anaconda3\\pkgs\\opencv-4.5.5-py310h1e0e658_2\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

def faces(x):
    image,gray=Image.read_image(x)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.25,
        minNeighbors=4,
        minSize=(20, 20))
    face_region=[]
    # Iterate over the detected faces and draw rectangles around them
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Extract the face region from the image
        face_region.append(gray[y:y + h, x:x + w])

    # Save the output image
    cv2.imshow("After NMS", image)
    cv2.waitKey(0)
    return face_region
