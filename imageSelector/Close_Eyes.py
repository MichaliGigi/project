from imageSelector.ImageQuality import *


class Close_eyes(ImageQuality):
    def __init__(self):
        super(Close_eyes,self).__init__()



    def calculate_eye_aspect_ratio(self,eye):
        eye = np.array(eye, dtype=np.float32)
        # Compute the Euclidean distances between the two sets of
        # vertical eye landmarks (x, y)-coordinates
        A = np.linalg.norm(eye[1] - eye[5])
        B = np.linalg.norm(eye[2] - eye[4])

        # Compute the Euclidean distance between the horizontal
        # eye landmark (x, y)-coordinates
        C = np.linalg.norm(eye[0] - eye[3])

        # Compute the eye aspect ratio
        ear = (A + B) / (2.0 * C)
        return ear


    def detect_eyes(self,image):


        # Find all facial features in the image
        eyes_landmarks = image.get_eyes_landmarks()

        eyes_status = []
        amount_of_open_eyes = 0

        # Loop through each face
        for face in eyes_landmarks:


            # Calculate the eye aspect ratio for each eye
            left_ear = self.calculate_eye_aspect_ratio(face[0])
            right_ear = self.calculate_eye_aspect_ratio(face[1])

            # Define the threshold for closed eyes
            ear_threshold = 0.2

            # Determine the status of each eye (open or closed)
            if left_ear > ear_threshold:
                amount_of_open_eyes+=1
            if right_ear > ear_threshold:
                amount_of_open_eyes+=1

        return amount_of_open_eyes,len(eyes_landmarks)*2
    def calculateGrade(self, image):

        amount_of_open_eyes,amount_of_eyes = self.detect_eyes(image)
        if amount_of_eyes == 0:
            return 100
        grade = (amount_of_open_eyes / amount_of_eyes)*100
        return grade

