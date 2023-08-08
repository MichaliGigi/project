import cv2
import numpy as np
from Image import *

def calculate_color_score(image):
    # Resize the image to reduce processing time (optional)
    resized_image = cv2.resize(image, (200, 200))

    # Convert the image from BGR to RGB
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

    # Reshape the image to a 2D array of pixels
    pixels = rgb_image.reshape((-1, 3))

    # Convert the pixel values to float32
    pixels = np.float32(pixels)

    # Define the criteria for k-means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # Set the number of clusters (dominant colors) to extract
    num_clusters = 8

    # Perform k-means clustering to find the dominant colors
    _, labels, centers = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Count the occurrences of each label (cluster)
    counts = np.bincount(labels.flatten())

    # Calculate the percentage of each dominant color in the image
    color_percentages = counts / len(labels)

    # Calculate the color score as the sum of squared color percentages
    color_score = np.sum(color_percentages ** 2)

    return color_score
for i in range(42):
    # Read the image
    image, gray = Image.read_image(i)

    # Calculate the color score of the image
    score = calculate_color_score(image)

    # Print the color score
    print("picture:",i,"Color score:", score*100)
