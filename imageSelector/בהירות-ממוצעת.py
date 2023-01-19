from face_detection3 import *


x= 12

# Read the faces images
images=faces(x)
arr_of_mean = []
for face in images:
    # Calculate the average pixel value in one face
    (mean, _, _, _) = cv2.mean(face)
    arr_of_mean.append(mean)
# the average of all faces lightness
sum=0
for i in arr_of_mean:
    sum+=i
if len(arr_of_mean)!=0: # cannot divide by zero
    average = sum / len(arr_of_mean) #calculate average
    for i in arr_of_mean:
        if (abs(i-average)>20):
            print("not good")
            exit(0)
    print("good!")
else:  print("good!")
