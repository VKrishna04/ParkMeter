# To be used only during the development of the project to quickly get all the paths and project tree.
import os

# Specify the directory path
dir_path = os.path.dirname(__file__)
with open("dirpaths.txt", "w") as f:
    f.write("")
# Iterate through the directory tree
for root, _, files in os.walk(dir_path):
    for file in files:
        full_path = os.path.join(root, file)
        if ".git" not in full_path:
            with open("dirpaths.txt", "a") as f:
                f.write(os.path.join(root, file) + ",\n")
            # Print the full path of the file
            print(os.path.join(root, file))
