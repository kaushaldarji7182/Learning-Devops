# Use the os module to list all files in a directory and display their sizes.



import os

def list_files_with_sizes(directory):
    """Lists all files in the specified directory with their sizes in bytes."""
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    print(f"\nFiles in '{directory}':\n")
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):  # Check if it's a file
            file_size = os.path.getsize(file_path)  # Get file size in bytes
            print(f"{file_name} - {file_size} bytes")
    
if __name__ == "__main__":
    dir_path = r"C:\\Users\\Administrator\\Python\\ASSIGNMENTS"   # Change to your directory path
    list_files_with_sizes(dir_path)
