import sys
import os

directory_path = sys.argv[1]
total_size = 0

try:
    entries = os.listdir(directory_path)

    for entry in entries:
        entry_path = os.path.join(directory_path, entry)

        if os.path.isfile(entry_path):
            try:
                total_size += os.path.getsize(entry_path)
            except FileNotFoundError:
                print(f"Warning: File '{entry}' not found.")
            except PermissionError:
                print(f"Warning: No permission to access '{entry}'.")
        elif os.path.isdir(entry_path):
            for root, _, files in os.walk(entry_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        total_size += os.path.getsize(file_path)
                    except FileNotFoundError:
                        print(f"Warning: File '{file}' not found.")
                    except PermissionError:
                        print(f"Warning: No permission to access '{file}'.")

    print(f"Total size of all files: {total_size} bytes")

except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: No permission to read the directory.")
