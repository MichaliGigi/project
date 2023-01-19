from Image import *
import face_recognition

# Load the image
image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\{}.jpg".format(27))
image = imutils.resize(image, width=min(1000, image.shape[1]))

# Find all facial features in the image
face_landmarks_list = face_recognition.face_landmarks(image)

# Iterate through each facial feature set
for face_landmarks in face_landmarks_list:
    # Check if the mouth is open (indicating a smile)
    if face_landmarks["top_lip"][8] > face_landmarks["bottom_lip"][8]:
        print("Smiling!")
    else:
        print("Not smiling.")
    # Print the location of each facial feature in this image
    print(face_landmarks["top_lip"][8] , face_landmarks["bottom_lip"][8])