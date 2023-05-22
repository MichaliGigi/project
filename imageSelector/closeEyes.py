
from Image import *
def eyes(x):
    image, gray = Image.read_image(x)

    # Find all facial features in the image
    face_landmarks_list = face_recognition.face_landmarks(image)
    eyes_region = []

    # Loop through each face
    for face_landmarks in face_landmarks_list:
        this_eye = []
        # Get the coordinates of the eyes
        left_eye = face_landmarks['left_eye']
        right_eye = face_landmarks['right_eye']

        this_left_eye = []
        this_right_eye = []

        this_left_eye.append(image[left_eye[1][1] :left_eye[5][1] , left_eye[0][0] :left_eye[1][0] ])
        this_left_eye.append(image[left_eye[1][1]:left_eye[5][1], left_eye[2][0]:left_eye[3][0]])
        this_right_eye.append( image[right_eye[1][1] :right_eye[5][1], right_eye[0][0] :right_eye[1][0] ])
        this_right_eye.append(image[right_eye[1][1]:right_eye[5][1], right_eye[2][0]:right_eye[3][0]])

        this_left_eye.append(image[left_eye[1][1]:left_eye[5][1], left_eye[1][0]:left_eye[2][0]])
        this_right_eye.append(image[right_eye[1][1]:right_eye[5][1], right_eye[1][0]:right_eye[2][0]])

        this_eye.append(this_left_eye)
        this_eye.append(this_right_eye)
        eyes_region.append(this_eye)


    for pic in eyes_region:
        for eye in pic:


            # Splitting the images into B, G, R channels
            b0, g0, r0 = cv2.split(eye[0])
            b1, g1, r1 = cv2.split(eye[1])
            b2, g2, r2 = cv2.split(eye[2])

            # Calculating the average color values for each channel
            avg_b = (np.mean(b0) + np.mean(b1)) / 2.0
            avg_bb = np.mean(b2)
            avg_g = (np.mean(g0) + np.mean(g1)) / 2.0
            avg_gg = np.mean(g2)
            avg_r = (np.mean(r0) + np.mean(r1)) / 2.0
            avg_rr = np.mean(r2)

            # Checking if the average color values are close or different
            threshold = 10  # Define a threshold value to determine closeness
            print("Average color values: ", abs(avg_b - avg_bb), abs(avg_r-avg_rr), abs(avg_g-avg_gg))
          #  print("pupil: ", avg_bb, avg_gg, avg_rr)
            if abs(avg_b - avg_bb) < threshold and abs(avg_r-avg_rr) < threshold and abs(avg_g-avg_gg) < threshold:
                print("The average colors are close.")
            else:
                print("The average colors are different.")


for i in range(30):
    print(i)
    eyes(i)