import cv2
import dlib
import numpy as np
from scipy.spatial import distance

# Load pre-trained models
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')  # Update this path
face_recognizer = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

# Load and process images
image1 = cv2.imread("..\\Image_database\\{}.jpg".format(1))
image2 = cv2.imread("..\\Image_database\\{}.jpg".format(2))

# Detect faces and calculate face embeddings
def get_face_embeddings(image):
    faces = detector(image)
    face_landmarks = [shape_predictor(image, face) for face in faces]
    face_embeddings = [face_recognizer.compute_face_descriptor(image, landmarks) for landmarks in face_landmarks]
    return face_embeddings

embeddings1 = get_face_embeddings(image1)
embeddings2 = get_face_embeddings(image2)

# Calculate Euclidean distance between embeddings
distance = np.linalg.norm(np.array(embeddings1) - np.array(embeddings2))

# Set a threshold for similarity
threshold = 0.6  # Adjust this threshold as needed
if distance < threshold:
    print("Same person")
else:
    print("Different people")