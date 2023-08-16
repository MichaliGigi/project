import face_recognition
from Image import *

#im, _ = Image.read_image(202)
im=cv2.imread('..\\Image_database\\200.jpg')

my_face_encoding = face_recognition.face_encodings(im)[0]

im2=cv2.imread('..\\Image_database\\105.jpg')

#im2, _ = Image.read_image(110)
unknown_face_encoding = face_recognition.face_encodings(im2)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")
import face_recognition
# from Image import *
#
#
# def calculate_similarity(encoding1, encoding2):
#     # Calculate the Euclidean distance between the two face encodings
#     distance = face_recognition.face_distance([encoding1], encoding2)[0]
#
#     # Convert the distance to a similarity percentage (higher similarity -> lower distance)
#     similarity_percentage = (1 - distance) * 100
#
#     return similarity_percentage
#
# for i in range(110,116):
#     print(i, i+1)
#     im, _ = Image.read_image(i)
#     my_face_encoding = face_recognition.face_encodings(im)[0]
#
#     im2, _ = Image.read_image(i+1)
#     unknown_face_encoding = face_recognition.face_encodings(im2)[0]
#
#     similarity_percentage = calculate_similarity(my_face_encoding, unknown_face_encoding)
#
#     print(f"Similarity percentage: {similarity_percentage:.2f}%")
#
#     # You can set a threshold value to determine whether the faces are considered similar or not
#     threshold = 70  # Adjust this value as needed
#
#     if similarity_percentage >= threshold:
#         print("It's a picture of me!")
#     else:
#         print("It's not a picture of me!")
import cv2
import numpy as np
#
# from Image import *
#
# # Load the LBPH face recognizer model
# rec = cv2.face.LBPHFaceRecognizer_create()
#
# # Load the face encodings and corresponding labels for training
# # You need to replace these with your actual data
# faces_data = np.load('faces_data.npy', allow_pickle=True).item()
#
# # Train the recognizer using the loaded data
# rec.train(list(faces_data['encodings']), np.array(faces_data['labels']))
#
# # Load the images and their encodings
# im, _ = Image.read_image(105)
# my_face_encoding = face_recognition.face_encodings(im)[0]
#
# im2, _ = Image.read_image(107)
# unknown_face_encoding = face_recognition.face_encodings(im2)[0]
#
# # Compare the two face encodings using the LBPH face recognizer
# label, confidence = rec.predict(my_face_encoding)
#
# # Calculate the similarity percentage based on confidence (lower confidence -> higher similarity)
# similarity_percentage = (1 - (confidence / 400)) * 100
#
# print(f"Similarity percentage: {similarity_percentage:.2f}%")
#
# # You can set a threshold value to determine whether the faces are considered similar or not
# threshold = 70  # Adjust this value as needed
#
# if similarity_percentage >= threshold:
#     print("It's a picture of me!")
# else:
#     print("It's not a picture of me!")
#
