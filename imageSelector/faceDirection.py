from imageSelector.ImageQuality import *


class FaceDirection(ImageQuality):
    def __init__(self):
        super(FaceDirection, self).__init__()

    def calculateGrade(self, image):
        im, _ = image.get_image()
        face_landmarks_list = image.get_face_landmarks()
        if len(face_landmarks_list) == 0:
            return 100
        grade = 0
        for landmarks in face_landmarks_list:

            # Assuming 'top_lip' contains multiple points and 'left_cheek' and 'right_cheek' are single points
            left_lip_point = landmarks['top_lip'][0]  # Left point on the lips
            right_lip_point = landmarks['bottom_lip'][0]  # Right point on the lips
            left_cheek_point = landmarks['chin'][4]  # Left cheek point
            right_cheek_point = landmarks['chin'][12]  # Right cheek point
            nose_point = landmarks['nose_bridge'][3]  # Get the specific point

            distance_left = self.euclidean_distance(left_lip_point, left_cheek_point)
            distance_right = self.euclidean_distance(right_lip_point, right_cheek_point)

            # if the face look straight or the nose[0] is in the central  1/5 of the image
            if (max(float(distance_left.real), float(distance_right.real)) / min(float(distance_left.real),float(distance_right.real)) < 2.5 or
                    (im.shape[1] / 5)*2 < nose_point[0] < (im.shape[1] / 5) * 3):
                grade += 100
            else:

                image_width = im.shape[1] / 2
                # cheak if the face is in the left or right side of the image
                if distance_left.real < distance_right.real:
                    # Calculate the score based on nose position
                    if nose_point[0] <= image_width:
                        grade += 100 - (100 * nose_point[0] / (image_width))
                    else:
                        #
                        grade += 100
                else:
                    # Calculate the score based on nose position
                    if nose_point[0] >= image_width:
                        grade += 100 - (100 * (image_width * 2 - nose_point[0]) / (image_width * 2))
                    else:
                        grade += 100
            # # Draw points on the image
            # for point in [left_lip_point, right_lip_point, left_cheek_point, right_cheek_point, nose_point]:
            #     if point is not None:
            #         cv2.circle(im, point, 2, (0, 255, 0), -1)

        return grade / len(face_landmarks_list)

    # Calculate the Euclidean distance between two points
    def euclidean_distance(self, point1, point2):
        return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

