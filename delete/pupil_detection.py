from Image import *
import detect_eyes
# Load the eye image
eye_image = detect_eyes.eyes(1)

# Apply a Gaussian blur to the image to reduce noise
# gray = cv2.GaussianBlur(gray, (5, 5), 0)
for gray in eye_image:
    #gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use the Hough Circle Transform to detect circles in the image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

    # Make sure at least one circle was detected
    if circles is not None:
        # Convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # Draw the circles on the original image
        for (x, y, r) in circles:
            cv2.circle(gray, (x, y), r, (0, 255, 0), 2)
            cv2.circle(gray, (x, y), 2, (0, 0, 255), 3)

        # Show the image with the detected circles
        cv2.imshow("Pupil Detection", gray)
        cv2.waitKey(0)

    else:
        print("No circles found")

# Clean up
cv2.destroyAllWindows()