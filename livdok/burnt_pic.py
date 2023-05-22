import numpy as np
from PIL import Image
from Image import *

# Open the image
im, gray = Image.read_image(24)

# Convert the image to a numpy array
im_np = np.array(im)

# Flatten the image to a 1D array
im_flat = im_np.flatten()

# Calculate the average and standard deviation of the pixel values
average = np.mean(im_flat)
std_dev = np.std(im_flat)
print("Average: {}".format(average))
print("Standard deviation: {}".format(std_dev))

# Check if the image is burnt
if average > 200 and std_dev < 20:
    print("This image is burnt.")
else:
    print("This image is not burnt.")