from Image import *
# Load the pre-trained model for body detection
model = cv2.dnn.readNetFromCaffe('body_detection_model.prototxt', 'body_detection_model.caffemodel')
for x in range(22):

    image, gray = Image.read_image(x)
    # Set the input image for the model
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
    model.setInput(blob)

    # Run the model and get the output
    output = model.forward()

    # Loop through the output and draw a rectangle around the detected body
    for i in range(output.shape[2]):
        confidence = output[0, 0, i, 2]
        if confidence > 0.5:
            x1 = int(output[0, 0, i, 3] * image.shape[1])
            y1 = int(output[0, 0, i, 4] * image.shape[0])
            x2 = int(output[0, 0, i, 5] * image.shape[1])
            y2 = int(output[0, 0, i, 6] * image.shape[0])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Show the output image
    cv2.imshow('Image', image)
    cv2.waitKey(0)
