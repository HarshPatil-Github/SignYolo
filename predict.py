from ultralytics import YOLO
import os
import random

# Initialize the model with your configuration file
model = YOLO("runs/detect/train11/weights/best.pt")

# Get a list of all image files in the totalDataTest directory
image_files = [f for f in os.listdir("totalDataTest") if f.endswith(('.jpg', '.png'))]  # adjust this line to include other image file types if necessary

# Randomly select 10 image files
selected_images = random.sample(image_files, 10)

# Perform prediction on each selected image
for selected_image in selected_images:
    results = model.predict(os.path.join("totalDataTest", selected_image))
    
    # The results object will contain the predictions
    for pred in results:
        print(f"Image: {selected_image}, Predictions: {pred}")
