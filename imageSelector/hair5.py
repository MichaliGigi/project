from Image import *  # Import the Image module as per your code


def calculate_pixel_counts(image, bounding_box):
    x1, y1, x2, y2 = bounding_box
    # extract the region of interest from the image
    region = image[y1:y2, x1:x2]

    # Count dark and light pixels
    dark_pixel_count = np.sum(region < 50)
    light_pixel_count = np.sum(region >= 50)

    return dark_pixel_count, light_pixel_count


def process_image(image):
    face_locations = face_recognition.face_locations(image)

    # Loop through each face
    for (top, right, bottom, left) in face_locations:
        eye_level = int(top + (bottom - top) * 0.4)
        mouth_level = int(top + (bottom - top) * 0.8)
        face_frame_right = right
        face_frame_left = left

        frame_top_left = (face_frame_left, eye_level)
        frame_bottom_right = (face_frame_right, mouth_level)

        cv2.rectangle(image, frame_top_left, frame_bottom_right, (0, 0, 255), 2)

        bounding_box = (face_frame_left, eye_level, face_frame_right, mouth_level)

        dark_pixel_count, light_pixel_count = calculate_pixel_counts(image, bounding_box)
        precen = dark_pixel_count / (dark_pixel_count + light_pixel_count)
        print("Percentage of dark pixels:", precen)
        if precen > 0.3:
            print("there is hair")
        else:
            print("there is no hair")

        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow('Marked Areas', image)
    cv2.waitKey(0)


def main():
    for x in range(91, 94):
        image, _ = Image.read_image(x)  # Load image using your Image class, modify this part as needed
        process_image(image)


if __name__ == "__main__":
    main()
