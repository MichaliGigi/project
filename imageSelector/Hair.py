from imageSelector.ImageQuality import *


class Hair(ImageQuality):
    def __init__(self):
        super(Hair, self).__init__()

    def calculateGrade(self, image):

        #face_locations = face_recognition.face_locations(image)
        face_locations = image.get_face_location()
        if len(face_locations) == 0:
            return 100
        im,_=image.get_image()
        amount_of_faces_covered_hair = 0
        # Loop through each face
        for (top, right, bottom, left) in face_locations:
            eye_level = int(top + (bottom - top) * 0.4)
            mouth_level = int(top + (bottom - top) * 0.8)
            face_frame_right = right
            face_frame_left = left

           # frame_top_left = (face_frame_left, eye_level)
           # frame_bottom_right = (face_frame_right, mouth_level)

            #cv2.rectangle(im, frame_top_left, frame_bottom_right, (0, 0, 255), 2)

            bounding_box = (face_frame_left, eye_level, face_frame_right, mouth_level)

            dark_pixel_count, light_pixel_count = self.calculate_pixel_counts(im, bounding_box)
            precen = dark_pixel_count / (dark_pixel_count + light_pixel_count)
            if precen > 0.3:
                amount_of_faces_covered_hair += 1
        return 100-amount_of_faces_covered_hair / len(face_locations)*100

            #cv2.rectangle(im, (left, top), (right, bottom), (0, 255, 0), 2)

        # cv2.imshow('Marked Areas', im)
        # cv2.waitKey(0)

    def calculate_pixel_counts(self,image, bounding_box):
        x1, y1, x2, y2 = bounding_box
        # extract the region of interest from the image
        region = image[y1:y2, x1:x2]

        # Count dark and light pixels
        dark_pixel_count = np.sum(region < 50)
        light_pixel_count = np.sum(region >= 50)

        return dark_pixel_count, light_pixel_count
