import os

# Mapping dictionary
mapping = {
    'व': 'v',
    'श': 'sh',
    'स': 's',
    'ह': 'h',
    'ळ': 'l',
    'क्ष': 'ksh',
    'ज्ञ': 'gya'
}

# Path to your subfolder
subfolder_path = 'Data/क्ष'

# Iterate over the files in the subfolder
for filename in os.listdir(subfolder_path):
    # Iterate over the keys in the mapping dictionary
    for key in mapping:
        # If the filename starts with the key
        if filename.startswith(key):
            # Replace the key with its corresponding value in the filename
            new_filename = filename.replace(key, mapping[key])
            # Rename the file
            os.rename(os.path.join(subfolder_path, filename), os.path.join(subfolder_path, new_filename))