from Image import *


class Face:

    def face(x):
        image, gray = Image.read_image(x)
        # Find all the faces in the image
        face_locations = face_recognition.face_locations(gray)

        # Initialize an empty list to store the cropped face images
        face_images = []

        # Loop through each face location and crop the rectangular region
        for i, face_location in enumerate(face_locations):
            top, right, bottom, left = face_location
            face_image = image[top:bottom, left:right]
            face_images.append(face_image)

        # Return the list of cropped face images
        return face_images
