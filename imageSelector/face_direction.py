from face import *
for i in range(5):
    image, gray = Image.read_image(44)
    faces= Face.face(44)
    ellipses = []
    for face in faces:

        # Convert the face to grayscale
        gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        # Convert grayscale image to binary
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # Find contours in the binary image
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # Fit ellipse to the largest contour
        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)
            ellipse = cv2.fitEllipse(largest_contour)

            # Draw the ellipse on the image
            cv2.ellipse(face, ellipse, (0, 255, 0), 2)

            # Add the ellipse to the list
            ellipses.append(ellipse)

        # Display the image
        cv2.imshow("Image", face)
        cv2.waitKey(0)
