import tensorflow as tf
import cv2
# Load the TensorFlow Object Detection API model
model = tf.saved_model.load('C:\\Users\\User\\anaconda3\\envs\\project\\Lib\\site-packages\\tensorflow\\python\\saved_model')

# Load an image
image = cv2.imread("C:\\Users\\User\\Desktop\\Image database-project\\{}.jpg".format(5))

# Run the model to detect objects in the image
detection_results = model(image)

# Print the results
print(detection_results)
