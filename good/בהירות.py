from face_detection3 import *
# Load the image
image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\11.jpg")

# Segment the main object from the image (replace this with your own object segmentation code)
mask = ...

# Apply the mask to the image to segment the main object
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Calculate the average brightness of the segmented object
(b, g, r) = cv2.mean(segmented_image)
brightness = (r + g + b) / 3

# Print the average brightness
print(f'Average brightness: {brightness:.2f}')
