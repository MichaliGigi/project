from Image import *


def calculate_eye_aspect_ratio(eye):
    eye = np.array(eye, dtype=np.float32)
    # Compute the Euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])

    # Compute the Euclidean distance between the horizontal
    # eye landmark (x, y)-coordinates
    C = np.linalg.norm(eye[0] - eye[3])

    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear


def detect_eyes(image_path):
    image, gray = Image.read_image(image_path)


    # Find all facial features in the image
    face_landmarks_list = face_recognition.face_landmarks(image)

    eyes_status = []

    # Loop through each face
    for face_landmarks in face_landmarks_list:
        # Get the coordinates of the eyes
        left_eye = face_landmarks['left_eye']
        right_eye = face_landmarks['right_eye']

        # Calculate the eye aspect ratio for each eye
        left_ear = calculate_eye_aspect_ratio(left_eye)
        right_ear = calculate_eye_aspect_ratio(right_eye)

        # Define the threshold for closed eyes
        ear_threshold = 0.2

        # Determine the status of each eye (open or closed)
        left_eye_status = "Open" if left_ear > ear_threshold else "Closed"
        right_eye_status = "Open" if right_ear > ear_threshold else "Closed"

        eyes_status.append((left_eye_status, right_eye_status))
    return eyes_status
def cal_grade(i):

    eyes_status = detect_eyes(i)
    if (len(eyes_status)==0):
        return 100
    counter = 0
    for status in eyes_status:
        left_eye_status, right_eye_status = status
        if left_eye_status == "Open":
            counter += 1
        if right_eye_status == "Open":
            counter += 1
    grade = counter / (len(eyes_status) * 2)*100
    return grade


# Call the function with the image path
for i in range(42):
    print(i)
    print("grade" +str(cal_grade(i)))
