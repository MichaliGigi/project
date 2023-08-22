import cv2
import dlib
import numpy as np
import face_recognition

from imageSelector.Image import Image

#
# # Detect faces and calculate face embeddings
# def get_face_embeddings(image):
#     faces = detector(image)
#     face_landmarks = [shape_predictor(image, face) for face in faces]
#     face_embeddings = [face_recognizer.compute_face_descriptor(image, landmarks) for landmarks in face_landmarks]
#     return faces, face_embeddings
#
# # Load pre-trained models
# detector = dlib.get_frontal_face_detector()
# shape_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# face_recognizer = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
#
# # Load and process images
# image1 = cv2.imread("C:\\Users\\User\\Downloads\\tryy\\IMG-20230816-WA0104.jpg")
# image2 = cv2.imread("C:\\Users\\User\\Downloads\\tryy\\IMG-20230816-WA0038.jpg")
#
# faces1, embeddings1 = get_face_embeddings(image1)
# faces2, embeddings2 = get_face_embeddings(image2)
#
# # Compare all combinations of embeddings
# for i, emb1 in enumerate(embeddings1):
#     for j, emb2 in enumerate(embeddings2):
#         # Calculate Euclidean distance between embeddings
#         distance = np.linalg.norm(np.array(emb1) - np.array(emb2))
#
#         # Set a threshold for similarity
#         threshold = 0.6  # Adjust this threshold as needed
#         if distance < threshold:
#             # Draw rectangles around the detected faces
#             color = (0, 255, 0)  # Green for matching faces
#             if i == 0:  # If it's the first recognized face in image1, mark it red
#                 color = (0, 0, 255)  # Red
#             cv2.rectangle(image1, (faces1[i].left(), faces1[i].top()), (faces1[i].right(), faces1[i].bottom()), color, 2)
#             cv2.rectangle(image2, (faces2[j].left(), faces2[j].top()), (faces2[j].right(), faces2[j].bottom()), color, 2)
#             print("Same person in images, face {} in image1 and face {} in image2".format(i, j))
#         else:
#             print("Different people in images, face {} in image1 and face {} in image2".format(i, j))
#
# # Display the images with rectangles around faces
# cv2.imshow("Image 1 with Faces", image1)
# cv2.imshow("Image 2 with Faces", image2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

im1=Image("C:\\Users\\User\\Downloads\\tryy\\IMG-20230816-WA0063.jpg").get_original_image()

my_faces_encoding = face_recognition.face_encodings(im1)
im2=Image("C:\\Users\\User\\Downloads\\tryy\\IMG-20230816-WA0099.jpg").get_original_image()
my_faces_encoding2 = face_recognition.face_encodings(im2)


for i_my_face,my_face in enumerate(my_faces_encoding):
    for i_face,face in enumerate(my_faces_encoding2):
        results = face_recognition.compare_faces([my_face], face)
        #if the face is already in the list
        if results[0] == True:
            print("Same person")
            # Cut out and display the first recognized face from image1
            face_location = face_recognition.face_locations(im1)[i_my_face]
            top, right, bottom, left = face_location
            recognized_face = im1[top:bottom, left:right]

            cv2.imshow("Recognized Face", recognized_face)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break

    else:
        print("Different people")



