from Image import *
img1, gray1 = Image.read_image(20)
img2, gray2 = Image.read_image(18)
# Initialize the SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# Find keypoints and descriptors in the images
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# Initialize the FLANN matcher
index_params = dict(algorithm=0, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Match the descriptors in the two images
matches = flann.knnMatch(des1, des2, k=2)

# Filter the matches using a ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Calculate the similarity score based on the number of good matches
similarity = len(good_matches) / max(len(kp1), len(kp2)) * 100

print(similarity)
