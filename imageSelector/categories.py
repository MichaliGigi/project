
from imageSelector.Image import *


class Categories:
    def __init__(self):
        self.groups = []

    def fillCategory(self, image):
        _, gray = image.get_image()

        hist = self.compute_histogram(gray)

        correlations = []
        # compare image1 with all images in groups
        for i, group in enumerate(self.groups):
            correlations.append(self.compare_histograms(hist, group))
            #correlation = self.compare_histograms(hist, group)
           # print(correlation)
            #if correlation > 0.4:
             #   return i
        if len(correlations) > 0 and max(correlations) > 0.3:
            return correlations.index(max(correlations))
        else:
            self.groups.append(hist)
            return len(self.groups) - 1

    def compute_histogram(self, image):
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        return hist

    def compare_histograms(self, hist1, hist2, method=cv2.HISTCMP_CORREL):
        return cv2.compareHist(hist1, hist2, method)

# c=Categories()
# print(c.fillCategory(Image("C:\\Users\\User\\Downloads\\x\\1691584607348.jpg")))
# print(c.fillCategory(Image("C:\\Users\\User\\Downloads\\x\\IMG-20230816-WA0048.jpg")))
# print(c.fillCategory(Image("C:\\Users\\User\\Downloads\\x\\IMG-20230816-WA0062.jpg")))
# print(c.fillCategory(Image("C:\\Users\\User\\Downloads\\x\\IMG-20230816-WA0095.jpg")))