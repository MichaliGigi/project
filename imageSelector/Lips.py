import cv2


class Lips:
    def __init__(self, face_landmarks, gray):
        self.gray = gray
        self.face_landmarks = face_landmarks

    def getLips(self):
        self.rect_lips =[]
        for face in self.face_landmarks:
            # cut the image between the lips points
            self.rect_lips.append(self.gray[face['top_lip'][4][1]:face['bottom_lip'][8][1],
                                  face['top_lip'][2][0]:face['bottom_lip'][10][0]])
        return self.rect_lips

