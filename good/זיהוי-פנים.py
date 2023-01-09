#מזהה יפה מאד דמויות מרכזיות
import os
from Image import *

# Load the Haar cascade classifier for detecting faces
cv2_base_dir = os.path.dirname(os.path.abspath(cv2.__file__))
haar_model = os.path.join(cv2_base_dir,'C:\\Users\\User\\anaconda3\\pkgs\\opencv-4.5.5-py310h1e0e658_2\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')

#'\data\haarcascade_frontalface_default.xml')

faceCascade = cv2.CascadeClassifier(haar_model)
for x in range(17):

    image,gray=Image.read_image(x)


    #faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale( gray,scaleFactor=1.25,minNeighbors=3,minSize=(30, 30))

    print("[INFO] Found {0} Faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("After NMS", image)
    cv2.waitKey(0)
