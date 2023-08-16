import csv
import os

from Image import *

titles={"path":0}


def compute_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

def compare_histograms(hist1, hist2, method=cv2.HISTCMP_CORREL):
    return cv2.compareHist(hist1, hist2, method)


def divide_groups():

    script_path = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the CSV file using os.path.join
    csv_file_path = os.path.join(script_path, '..', 'manager', 'images_info.csv')
    # open the csv file to read and write



        csvreader = csv.reader(csvfile)
        next(csvreader)
        # define const name for row[0]
        for row in csvreader:
            image, gray = Image.read_image(row[titles["path"]])
            hist = compute_histogram(gray)

            # compare image1 with all images in groups
            for group in groups:
                correlation = compare_histograms(hist, group[0][1])
                print (correlation)

                if correlation>0.3:
                    group.append((i, hist))
                    break
            else:
                groups.append([(i, hist)])


image1, gray1 = Image.read_image("C:\\Users\\User\\PycharmProjects\\finalproject\\Image_database\\9.jpg")

# enter the first image to group 1
groups = [[compute_histogram(gray1)]]

divide_groups()


i=0
for group in groups:
    print(f"Group {i}: ", end="")
    for image in group:
        print(image[0], end=" ")
    i+=1


