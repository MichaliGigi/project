#עובד אבל לא מדויק בערך 80 אחוז עובד
# import the necessary packages
from Image import *

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for x in range(22):

	image,gray=Image.read_image(x)
	orig = image.copy()

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(gray, winStride=(2,2),padding=(8, 8), scale=1.3)

	# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
	# draw the final bounding boxes
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

	# show the output images
	cv2.imshow("After", image)
	cv2.waitKey(0)
cv2.destroyAllWindows()