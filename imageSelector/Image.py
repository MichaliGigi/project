# import the necessary packages
from Libraries import *
class Image:

    def read_image(x):
        # Load the input image
        #image = cv2.imread("..\\Image_database\\{}.jpg)".format(x))
        image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\{}.jpg".format(x), cv2.COLOR_BGR2RGB)

        # Resize the image
        image = imutils.resize(image, width=min(1000, image.shape[1]))

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image, gray
