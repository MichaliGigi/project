from Libraries import *
class Face:
    def __init__(self,image,gray):
        self.image = image
        self.gray = gray

    def face_rec(self):
        # Find all the faces in the image
        face_locations = face_recognition.face_locations(self.gray)

        # Initialize an empty list to store the cropped face images
        face_images = []

        # Loop through each face location and crop the rectangular region
        for i, face_location in enumerate(face_locations):
            top, right, bottom, left = face_location
            face_image = self.image[top:bottom, left:right]
            face_images.append(face_image)

        # Return the list of cropped face images
        return face_images,face_locations
    def face_landmarks(self):
        # Find all facial features in the image
        face_landmarks_list = face_recognition.face_landmarks(self.image)
        return face_landmarks_list