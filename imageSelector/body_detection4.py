from Image import *

# Initializing the HOG person
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
for x in range(22):
    image, gray = Image.read_image(x)

    # Detecting all humans
    (humans, _) = hog.detectMultiScale(image,
                                       winStride=(5, 5),
                                       padding=(8, 8),
                                       scale=1.21)
    # getting no. of human detected
    print('Human Detected : ', len(humans))

    # Drawing the rectangle regions
    for (x, y, w, h) in humans:
        cv2.rectangle(image, (x, y),
                      (x + w, y + h),
                      (0, 0, 255), 2)

    # Displaying the output Image
    cv2.imshow("Image", image)
    cv2.waitKey(0)

cv2.destroyAllWindows()