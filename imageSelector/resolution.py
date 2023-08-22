import math

from imageSelector.ImageQuality import *


class Resolution(ImageQuality):

    def __init__(self):
        super(Resolution, self).__init__()

    def calculateGrade(self, image):
        original_image = image.get_original_image()
        height, width = original_image.shape[:2]

        min_resolution = 100  # Define the minimum resolution for a non-zero score
        max_resolution = 5000  # Define the maximum resolution you want to consider

        # Clip width and height within bounds
        width = max(min(width, max_resolution), min_resolution)
        height = max(min(height, max_resolution), min_resolution)

        # Calculate the score using a logarithmic function and scale it to 0-100
        scaled_score = (math.log1p(min(width, height) / min_resolution) / math.log1p(
            max_resolution / min_resolution)) * 100
        return scaled_score

# x=Resolution()
# print("grade ",x.calculateGrade(Image("C:\\Users\\User\\Downloads\\tryy\\IMG-20230816-WA0063.jpg")))
# print(x.calculateGrade(Image("C:\\Users\\User\\Downloads\\tryy\\IMG-20230816-WA0066.jpg")))
# print(x.calculateGrade(Image("C:\\Users\\User\\Downloads\\tryy\\IMG-20230816-WA0067.jpg")))
# print(x.calculateGrade(Image("C:\\Users\\User\\Downloads\\tryy\\IMG-20230816-WA0069.jpg")))
# print(x.calculateGrade(Image("C:\\Users\\User\\Downloads\\tryy\\IMG-20230816-WA0070.jpg")))
# print(x.calculateGrade(Image("C:\\Users\\User\\PycharmProjects\\finalproject\\Image_database\\IMG_0927.JPG")))
# print(x.calculateGrade(Image("C:\\Users\\User\\PycharmProjects\\finalproject\\Image_database\\IMG_0928.JPG")))
# print(x.calculateGrade(Image("C:\\Users\\User\\PycharmProjects\\finalproject\\Image_database\\IMG_0929.JPG")))
# print(x.calculateGrade(Image("C:\\Users\\User\\PycharmProjects\\finalproject\\Image_database\\IMG_0930.JPG")))
# print(x.calculateGrade(Image("C:\\Users\\User\\PycharmProjects\\finalproject\\Image_database\\IMG_0931.JPG")))
# print(x.calculateGrade(Image("C:\\Users\\User\\PycharmProjects\\finalproject\\Image_database\\IMG_0932.JPG")))
# print(x.calculateGrade(Image("C:\\Users\\User\\PycharmProjects\\finalproject\\Image_database\\114.JPG")))
# print(x.calculateGrade(Image("C:\\Users\\User\\PycharmProjects\\finalproject\\Image_database\\13.jpg")))

