#Write a script to automate file creation and deletion in a specified directory.


import os
import time

def create_files(directory, prefix, num_files, extension="txt"):
    """Creates multiple files in the specified directory."""
    if not os.path.exists(directory):
        os.makedirs(directory)  # Create directory if it doesn't exist
        print(f"Directory '{directory}' created.")

    for i in range(1, num_files + 1):
        file_path = os.path.join(directory, f"{prefix}_{i}.{extension}")
        with open(file_path, "w") as f:
            f.write(f"File {i} created at {time.ctime()}\n")
        print(f"Created: {file_path}")

def delete_files(directory, prefix=None):
    """Deletes files in the specified directory. If prefix is given, deletes only matching files."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    deleted_files = 0
    for file_name in os.listdir(directory):
        if prefix is None or file_name.startswith(prefix):
            file_path = os.path.join(directory, file_name)
            os.remove(file_path)
            deleted_files += 1
            print(f"Deleted: {file_path}")

    if deleted_files == 0:
        print("No matching files found to delete.")
    else:
        print(f"Total deleted files: {deleted_files}")

if __name__ == "__main__":
    dir_path = "C:\\Users\\Administrator\\Python\\ASSIGNMENTS"  
    file_prefix = "sample"
    num_of_files = 5

    # Create files
    create_files(dir_path, file_prefix, num_of_files)

    # Wait before deletion (optional)
    time.sleep(5)

    # Delete files
    delete_files(dir_path, file_prefix)
