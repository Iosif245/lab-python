import sys
import os

directory_path = sys.argv[1]

try:
    files = os.listdir(directory_path)
    files = [file for file in files if os.path.isfile(os.path.join(directory_path, file))]

    if not files:
        print("No files to rename in the directory.")
        sys.exit(0)

    for index, file in enumerate(files, start=1):
        old_path = os.path.join(directory_path, file)
        new_filename = f"file{index}{os.path.splitext(file)[1]}"
        new_path = os.path.join(directory_path, new_filename)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed '{file}' to '{new_filename}'")
        except FileNotFoundError:
            print(f"Error: File '{file}' not found.")
        except PermissionError:
            print(f"Error: No permission to rename file '{file}'.")
        except OSError as e:
            print(f"Error: {e}")

except FileNotFoundError:
    print("Error: Directory not found.")
except PermissionError:
    print("Error: No permission to read the directory.")
except OSError as e:
    print(f"Error: {e}")