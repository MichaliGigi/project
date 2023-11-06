from imageSelector.ImageQuality import *


class Hair(ImageQuality):
    def __init__(self):
        super(Hair, self).__init__()

    def calculateGrade(self, image):

        #face_locations = face_recognition.face_locations(image)
        face_locations = image.get_face_location()
        if len(face_locations) == 0:
            print("no face")
            return 100
        im,gray=image.get_image()
        amount_of_faces_covered_hair = 0
        # Loop through each face
        for(top, right, bottom, left) in face_locations:
            eye_level = int(top + (bottom - top) * 0.4)
            mouth_level = int(top + (bottom - top) * 0.8)
            face_frame_right = right
            face_frame_left = left


            bounding_box = (face_frame_left, eye_level, face_frame_right, mouth_level)
            dark_pixel_count, light_pixel_count = self.calculate_pixel_counts(gray, bounding_box)
            percent = dark_pixel_count / (dark_pixel_count + light_pixel_count)
            print("percent",percent)
            if percent > 0.05:
                amount_of_faces_covered_hair += min(percent*3,1)
        return 100-amount_of_faces_covered_hair / len(face_locations)*100



    def calculate_pixel_counts(self,image, bounding_box):
        x1, y1, x2, y2 = bounding_box
        # extract the region of interest from the image
        region = image[y1:y2, x1:x2]

        # Count dark and light pixels
        dark_pixel_count = np.sum(region < 50)
        light_pixel_count = np.sum(region >= 50)

        return dark_pixel_count, light_pixel_count
