from imageSelector.ImageQuality import *


class Smile(ImageQuality):
    def __init__(self):
        super(Smile, self).__init__()

    def calculateGrade(self, image):
        lips=image.get_rect_lips()

        # # Load the cascade for detecting faces
        #faces = image.get_faces()
        amount_of_smiles = 0
        for lip in lips:
            precent= self.calculate_bright_pixel_percentage(lip)
            if precent > 10:
                amount_of_smiles += 1

        # # i, gray = image.get_image()
        # # # Load the smile cascade classifier
        # # smile_cascade = cv2.CascadeClassifier("..\\imageSelector\\haarcascade_smile.xml")
        # #
        # # # Detect smiles in the face region
        # # x= len(smile_cascade.detectMultiScale(fa, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25)))
        #
        # if len(faces) == 0:
        #     return 100
        #
        # amount_of_smiles = 0
        # # Iterate through detected faces
        # for face in faces:
        #     # Extract the face region
        #
        #     # Load the smile cascade classifier
        #     smile_cascade = cv2.CascadeClassifier("..\\imageSelector\\haarcascade_smile.xml")
        #
        #     # Detect smiles in the face region
        #     if len(smile_cascade.detectMultiScale(face, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25)))>0:
        #         amount_of_smiles += 1
        return amount_of_smiles / (len(lips))*100

    def calculate_bright_pixel_percentage(self,image):
        total_pixels = image.size
        if total_pixels == 0:

            return 0
        mask = (image > 150).astype(int)  # Create binary mask
        bright_pixel_count = cv2.countNonZero(mask)

        bright_pixel_percentage = (bright_pixel_count / total_pixels) * 100
        return bright_pixel_percentage


