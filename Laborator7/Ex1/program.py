import sys
import os

directory_path = sys.argv[1]
file_extension = sys.argv[2]

try:
    file_list = os.listdir(directory_path)
    file_list = [file for file in file_list if file.endswith(file_extension)]
    for file in file_list:
        path = os.path.join(directory_path, file)
        try:
            opened_file = open(path, "r")
        except FileNotFoundError:
            print(f"Error: File '{file}' not found.")
        except PermissionError:
            print(f"Error: No permission to read file '{file}'.")
        else:
            print(opened_file.read())
        pass
except OSError:
    print("Error: Directory not found")
