from scipy.spatial import distance as dist
from Image import *
import face_recognition
#==============================================================================
def eye_aspect_ratio(eye):

    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio
    return ear
#==============================================================================


def eyes(x):
    EYE_AR_THRESH = 0.23
    COUNTER = 0
    image, gray = Image.read_image(x)
    # Find all facial features in the image
    face_landmarks_list = face_recognition.face_landmarks(image)
    eyes_region = []

    # Loop through each face
    for face_landmarks in face_landmarks_list:
        # Get the coordinates of the eyes
        left_eye = face_landmarks['left_eye']
        right_eye = face_landmarks['right_eye']
        leftEAR = eye_aspect_ratio(left_eye)
        rightEAR = eye_aspect_ratio(right_eye)

        # average the eye aspect ratio together for both eyes
        ear = (leftEAR + rightEAR) / 2.0

        # check to see if the eye aspect ratio is below the blink
        # threshold, and if so, increment the blink frame counter
        if ear < EYE_AR_THRESH:
            print(ear)
            COUNTER += 1
    return COUNTER

for x in range(36):
    print(x,eyes(x))

