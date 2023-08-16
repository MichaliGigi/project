from face import *


def detect_smiles(x):
    # Load the cascade for detecting faces
    faces = Face.face(x)

    # Iterate through detected faces
    for face in faces:
        # Extract the face region


        # Load the smile cascade classifier
        smile_cascade = cv2.CascadeClassifier( "haarcascade_smile.xml")

        # Detect smiles in the face region
        smiles = smile_cascade.detectMultiScale(face, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))

        # Check if any smiles are detected
        if len(smiles) > 0:
            print("Smiling face detected!")


# for i in range(27):
#     print(i)
#     detect_smiles(i)
detect_smiles(80)

