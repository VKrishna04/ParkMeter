import os

# Specify the directory path
dir_path = os.path.dirname(__file__)

# Iterate through the directory tree
for root, _, files in os.walk(dir_path):
    for file in files:
        # Print the full path of the file
        print(os.path.join(root, file))
