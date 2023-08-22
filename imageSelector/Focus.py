from imageSelector.ImageQuality import *


class Focus(ImageQuality):
    def __init__(self):
        super(Focus, self).__init__()

    def calculateGrade(self, image):
        # Load the image and convert it to grayscale
        _,gray = image.get_image()

        # Find the gradient magnitude and direction of the image
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        magnitude, direction = cv2.cartToPolar(sobelx, sobely, angleInDegrees=True)

        # Calculate the focus measure using the gradient magnitude
        focus_measure = cv2.Laplacian(magnitude, cv2.CV_64F).var()
        num_digits = len(str(int(focus_measure)))
        if num_digits < 3:
            grade = 0
        elif num_digits == 3:
            grade = min(50, (focus_measure / 999) * 50)
        elif num_digits == 4:
            grade = min(90, 50 + ((focus_measure - 1000) / 9000) * 40)
        elif num_digits == 5:
            grade = min(100, 90 + ((focus_measure - 10000) / 90000) * 10)
        else:
            grade = 100
        return grade

# x=Focus()
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

