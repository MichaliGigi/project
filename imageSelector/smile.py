from imageSelector.ImageQuality import *


class Smile(ImageQuality):
    def __init__(self):
        super(Smile, self).__init__()

    def calculateGrade(self, image):
        # Load the cascade for detecting faces
        faces = image.get_faces()
        # i, gray = image.get_image()
        # # Load the smile cascade classifier
        # smile_cascade = cv2.CascadeClassifier("..\\imageSelector\\haarcascade_smile.xml")
        #
        # # Detect smiles in the face region
        # x= len(smile_cascade.detectMultiScale(fa, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25)))

        if len(faces) == 0:
            return 100

        amount_of_smiles = 0
        # Iterate through detected faces
        for face in faces:
            # Extract the face region

            # Load the smile cascade classifier
            smile_cascade = cv2.CascadeClassifier("..\\imageSelector\\haarcascade_smile.xml")

            # Detect smiles in the face region
            if len(smile_cascade.detectMultiScale(face, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25)))>0:
                amount_of_smiles += 1
        print("smile grade: ", amount_of_smiles / (len(faces))*100)
        return amount_of_smiles / (len(faces))*100

u=Smile()
print(u.calculateGrade(Image("C:\\Users\\User\\Desktop\\Database\\IMG_0966.JPG")))
