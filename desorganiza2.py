import os
import shutil

# Get the current directory
current_dir = os.getcwd()

# Create a directory to store the removed files
removed_files_dir = os.path.join(current_dir, 'removed_files')
if not os.path.exists(removed_files_dir):
    os.makedirs(removed_files_dir)

# Iterate over each file and folder in the current directory
for file_or_folder in os.listdir(current_dir):
    # Get the full path of the file or folder
    file_or_folder_path = os.path.join(current_dir, file_or_folder)

    # If it is a file, move it to the removed_files directory
    if os.path.isfile(file_or_folder_path):
        shutil.move(file_or_folder_path, removed_files_dir)

    # If it is a folder, iterate over its contents
    elif os.path.isdir(file_or_folder_path):
        for root, dirs, files in os.walk(file_or_folder_path, topdown=False):
            # Move all the files in the folder to the removed_files directory
            for name in files:
                file_path = os.path.join(root, name)
                shutil.move(file_path, removed_files_dir)

            # Remove all the empty folders
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.rmdir(dir_path)

# Remove all the empty folders in the current directory
for root, dirs, files in os.walk(current_dir, topdown=False):
    for name in dirs:
        dir_path = os.path.join(root, name)
        os.rmdir(dir_path)