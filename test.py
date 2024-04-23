import torch
from torchvision import transforms
from PIL import Image
import os
import yaml
from ultralytics import YOLO

# Load the model
model = torch.hub.load('.', 'custom', path='runs/detect/train11/weights/best.pt', source='local') 
model.eval()

# Load the class labels from the yaml file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)
classes = config['names']  # adjust this line if the class names are stored under a different key in the yaml file

# Define the image transformations

# Directory containing the test images
test_dir = 'totalDataTest'

# Loop over the images in the test directory
for filename in os.listdir(test_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # adjust this line to include other image file types if necessary
        # Load and preprocess the image
        image = Image.open(os.path.join(test_dir, filename))


        # Perform the forward pass and get the output
        with torch.no_grad():
            outputs = model(image)

        # Process the output
        _, predicted = torch.max(outputs.data, 1)
        class_id = predicted.item()
        print(f'Image {filename}: {classes[class_id]}')