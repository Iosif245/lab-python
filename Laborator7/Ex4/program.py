import sys
import os

directory_path = sys.argv[1]
extensions_count = {}

try:
    files = os.listdir(directory_path)

    if not files:
        raise Exception("Error: No files found in the directory.")

    for file in files:
        if os.path.isfile(os.path.join(directory_path, file)):
            extension = file.split(".")[-1]
            if extension in extensions_count:
                extensions_count[extension] += 1
            else:
                extensions_count[extension] = 1

    if extensions_count:
        for extension, count in extensions_count.items():
            print(f"{extension}: {count}")
    else:
        raise Exception("Error: No files found in the directory.")

except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: No permission to read the directory.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
