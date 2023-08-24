# import the necessary packages
from Libraries import *
from imageSelector.Face import Face
from imageSelector.Eyes import Eyes


class Image:
    def __init__(self, path):
        self.path = path
        self.read_image()
        face=Face(self.image,self.gray)
        self.faces,self.face_location = face.face_rec()
        self.face_landmarks = face.face_landmarks()

        self.rect_lips=[]
        for face in self.face_landmarks:
            # cut the image between the lips points
            self.rect_lips.append(self.gray[face['top_lip'][4][1]:face['bottom_lip'][8][1],
                        face['top_lip'][2][0]:face['bottom_lip'][10][0]])



        self.pupil_region,self.eyes_landmarks=Eyes(self.face_landmarks,self.image).eyes()



    def read_image(self):

        try:
            # Load the input image
            self.original_image = cv2.imread(self.path)
            if self.original_image is None:
                print("Could not read input image--" + str(self.path))
                return

            # Resize the image
            self.image = imutils.resize(self.original_image, width=min(1000, self.original_image.shape[1]))

            # Convert the image to grayscale
            self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)


            print("Image read successfully--" + str(self.path))

        except Exception as e:
            print("Something went wrong while reading the image--" + str(self.path))

    def get_image(self):
        return self.image,self.gray
    def get_faces(self):
        return self.faces
    def get_face_landmarks(self):
        return self.face_landmarks
    def get_path(self):
        return self.path
    def get_pupil_region(self):
        return self.pupil_region
    def get_eyes_landmarks(self):
        return self.eyes_landmarks
    def get_original_image(self):
        return self.original_image
    def get_face_location(self):
        return self.face_location
    def get_rect_lips(self):
        return self.rect_lips



#w=Image("C:\\Users\\User\\Downloads\\x\\6P1A2540.jpg")