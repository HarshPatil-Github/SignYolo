import cv2
import os
import time

def capture_images(num_images, base_dir, class_name):
    # Create the directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Open the camera
    cap = cv2.VideoCapture(0)
    time.sleep(0.5)  # Wait for 500ms after starting the camera

    for i in range(num_images):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # Display the resulting frame
            cv2.imshow('Frame', frame)

            file_path = os.path.join(base_dir, f"{class_name}_{i}.jpg")
            cv2.imwrite(file_path, frame)
            print("Image captured and saved successfully as", file_path)
        else:
            print(f"Error: Failed to capture image {i} for class {class_name}.")

        # Wait for a key press to proceed to the next image
        if cv2.waitKey(100) & 0xFF == ord('q'):  # Reduced delay to 100ms
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    num_images = 100  # Number of images to capture
    base_dir = "Data"  # Base directory
    class_name = "ज्ञ"  # Class name

    base_dir = os.path.join(base_dir, class_name)
    capture_images(num_images, base_dir, class_name)