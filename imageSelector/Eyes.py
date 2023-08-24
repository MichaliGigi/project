
import cv2
class Eyes():
    def __init__(self,face_landmarks_list,image):
        self.face_landmarks_list=face_landmarks_list
        self.image=image
    def eyes(self):
        # Find all facial features in the image
        pupil_region = []
        eyes_landmarks = []

        # Loop through each face
        for face_landmarks in self.face_landmarks_list:
            # Get the coordinates of the eyes
            left_eye = face_landmarks['left_eye']
            right_eye = face_landmarks['right_eye']
            eyes_landmarks.append((left_eye,right_eye))

            pupil_region.append(self.image[left_eye[1][1]-5 :left_eye[5][1]+5 , left_eye[1][0]-5 :left_eye[2][0]+5 ])
            pupil_region.append(self.image[right_eye[1][1]-5 :right_eye[5][1]+5 , right_eye[1][0]-5 :right_eye[2][0]+5 ])

        return pupil_region,eyes_landmarks


