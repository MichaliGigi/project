#מזעזעעעעע
#לא עובד
import cv2
import imutils
for x in range(21):

    # Load the image and convert it to grayscale
    image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\{}.jpg".format(x), cv2.IMREAD_GRAYSCALE)


    # Resize the image
    image = imutils.resize(image, width=min(1000, image.shape[1]))

    # Pre-process the image to enhance its features
    image = cv2.GaussianBlur(image, (5,5), 0)
    image = cv2.Canny(image, 50, 150)

    # Use edge detection to find the contours of the object
    contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Analyze the object to determine if it is intact
    if len(contours) > 0:
      # Object is intact
      result = True
    else:
      # Object is not intact
      result = False

    print(result)
