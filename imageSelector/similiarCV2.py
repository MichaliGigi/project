from Image import *


image1, gray1 = Image.read_image(28)
image2, gray2 = Image.read_image(29)


# Compute the histograms
hist1 = cv2.calcHist([gray1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])



# Compare the histograms using the correlation coefficient
corr = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

# Calculate the percentage similarity
similarity = corr * 100

print(similarity)
