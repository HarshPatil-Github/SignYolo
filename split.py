import os
import random
import shutil

# Path to your data directory
data_dir = 'totalData'

# Get list of image files
image_files = [file for file in os.listdir(data_dir) if file.endswith('.jpg')]

# Filter out image files that have corresponding text files
valid_image_files = []
for image_file in image_files:
    text_file = image_file.replace('.jpg', '.txt')
    if os.path.exists(os.path.join(data_dir, text_file)):
        valid_image_files.append(image_file)

# Shuffle the list of image files
random.shuffle(valid_image_files)

# Calculate the number of samples for train and test sets
total_samples = len(valid_image_files)
train_size = int(0.8 * total_samples)
test_size = total_samples - train_size

# Divide the image files into train and test sets
train_image_files = valid_image_files[:train_size]
test_image_files = valid_image_files[train_size:]

# Move image files to train directory
train_dir = 'totalDataTrain'
os.makedirs(train_dir, exist_ok=True)
for file in train_image_files:
    shutil.move(os.path.join(data_dir, file), os.path.join(train_dir, file))

# Move text files to train directory
for file in train_image_files:
    text_file = file.replace('.jpg', '.txt')
    shutil.move(os.path.join(data_dir, text_file), os.path.join(train_dir, text_file))

# Create test directory
test_dir = 'totalDataTest'
os.makedirs(test_dir, exist_ok=True)

# Move image files to test directory
for file in test_image_files:
    shutil.move(os.path.join(data_dir, file), os.path.join(test_dir, file))

# Move text files to test directory
for file in test_image_files:
    text_file = file.replace('.jpg', '.txt')
    shutil.move(os.path.join(data_dir, text_file), os.path.join(test_dir, text_file))
