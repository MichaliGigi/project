from imageSelector.ImageQuality import *

class BrightnessFaces(ImageQuality):
    def __init__(self):
        super(BrightnessFaces, self).__init__()

    def calculateGrade(self, image):
        faces=image.get_faces()
        if len(faces)==0:
            return 100
        arr_of_mean = []
        for face in faces:
            # Calculate the average pixel value in one face
            (mean, _, _, _) = cv2.mean(face)

            arr_of_mean.append(mean)
        # the average of all faces lightness
        sum=0
        for i in arr_of_mean:
            sum+=i
        if len(arr_of_mean)!=0: # cannot divide by zero
            average = sum / len(arr_of_mean) #calculate average
            count=0
            for i in arr_of_mean:
                if (abs(i-average)> 15):
                    count+=1
            grade=100-(count/len(arr_of_mean))*100

        else:
            grade=100
        return grade
# x=BrightnessFaces()
# print(x.calculateGrade(Image("C:\\Users\\User\\Downloads\\IMG_0910.JPG")))
# print(x.calculateGrade(Image("C:\\Users\\User\\Downloads\\IMG_0923.JPG")))