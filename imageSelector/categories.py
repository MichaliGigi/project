
from imageSelector.Image import *
import matplotlib.pyplot as plt

class Categories:
    def __init__(self):
        self.groups = []

    def fillCategory(self, image):
          # Load the two images
        # image_path1 = 'C:\\Users\\User\\Downloads\\h\\IMG_0907.JPG'
        # image_path2 = 'C:\\Users\\User\\Downloads\\h\\IMG_0907.JPG'
        # image1 = cv2.imread(image_path1)
        # image2 = cv2.imread(image_path2)
        #
        # # Convert the images to RGB
        # image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        # image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

        # Calculate histograms
      #  hist1, _ = np.histogram(image1_rgb.ravel(), bins=256, range=[0, 256])
      #  hist2, _ = np.histogram(image2_rgb.ravel(), bins=256, range=[0, 256])

        # Normalize histograms
       # hist1 = hist1 / hist1.sum()
        #hist2 = hist2 / hist2.sum()

        # Calculate Chi-Squared Distance
        #chi_squared_distance = np.sum(
        #    (hist1 - hist2) ** 2 / (hist1 + hist2 + 1e-10)) # Adding a small value to avoid division by zero

        # Print the similarity measure
       # print(f"Chi-Squared Distance between the histograms: {chi_squared_distance}")

        # You can set a threshold value to determine whether the images are similar or not based on the chi-squared distance.
        # Smaller values indicate more similar images.

        im, gray = image.get_image()
        image_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

        hist = self.compute_histogram(image_rgb)

        correlations = []
        # compare image1 with all images in groups
        for i, group in enumerate(self.groups):
            correlations.append(self.compare_histograms(hist, group))

        if len(correlations) > 0 and min(correlations) < 0.3:#>0.3
            return correlations.index(min(correlations))
        else:
            self.groups.append(hist)
            return len(self.groups) - 1

    def compute_histogram(self, image):
        hist,_ = np.histogram(image.ravel(), bins=256, range=[0, 256])
        hist = hist / hist.sum()
        #hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        #hist = cv2.normalize(hist, hist).flatten()
        return hist

    def compare_histograms(self, hist1, hist2):#, method=cv2.HISTCMP_CORREL):
        chi_squared_distance = np.sum(
            (hist1 - hist2) ** 2 / (hist1 + hist2 + 1e-10))  # Adding a small value to avoid division by zero
        print(f"Chi-Squared Distance between the histograms: {chi_squared_distance}")
        return chi_squared_distance
        #return cv2.compareHist(hist1, hist2, method)
#
# x=Categories()
# #x.fillCategory(Image("C:\\Users\\User\\Downloads\\esrim\\6P1A2901.jpg"))
# #x.fillCategory(Image("C:\\Users\\User\\Downloads\\esrim\\IMG-20230816-WA0093.jpg"))
# x.fillCategory(Image("C:\\Users\\User\\Downloads\\59.jpg"))
