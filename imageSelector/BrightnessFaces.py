from face import *


def brightness(image):

    # Read the faces images
    images = Face.face(image)
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
        count=0
        for i in arr_of_mean:
            if (abs(i-average)>20):
                count+=1
        grade=100-(count/len(arr_of_mean))*100

    else:
        grade=100
    return grade
for i in range(4, 23):
    print(str(i)+"the graed is:"+str(brightness(i))
            )
