import os
import shutil

folder_path = "sample files"

files = os.listdir(folder_path)

text_folder = os.path.join(folder_path, "Text_Files")
image_folder = os.path.join(folder_path, "Images")
python_folder = os.path.join(folder_path, "Python_Files")

os.makedirs(text_folder, exist_ok=True)
os.makedirs(image_folder, exist_ok=True)
os.makedirs(python_folder, exist_ok=True)

for file in files:
    source = os.path.join(folder_path, file)

    if os.path.isfile(source):
        if file.endswith(".txt"):
            destination = os.path.join(text_folder, file)
            shutil.move(source, destination)

        elif file.endswith((".jpg", ".jpeg", ".png")):
            destination = os.path.join(image_folder, file)
            shutil.move(source, destination)

        elif file.endswith(".py"):
            destination = os.path.join(python_folder, file)
            shutil.move(source, destination)

print("Files organized successfully!")