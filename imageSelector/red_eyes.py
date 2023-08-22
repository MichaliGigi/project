
from imageSelector.ImageQuality import *


class Red_eyes(ImageQuality):
    def __init__(self):
        super(Red_eyes,self).__init__()

    def calculateGrade(self, image):
        # Find all facial features in the image
        eyes_region = image.get_eyes_region()
        if len(eyes_region) == 0:
            return 100
        amount_of_red = 0
        # Loop through each eye
        for pic in eyes_region:
            b, g, r = cv2.split(pic)
            tolerance = 50
            counter = 0
            num_of_red = 10
            # iterate through all pixels in the image
            for i in range(r.shape[0]):
                for j in range(r.shape[1]):
                    # get the RGB values of the current pixel
                    red, green, blue = r[i][j], g[i][j], b[i][j]
                    if red > green + tolerance and red > blue + tolerance:
                        counter += 1
            if counter > num_of_red:
                amount_of_red += 1
        return 100-(amount_of_red/(len(eyes_region)*100))



