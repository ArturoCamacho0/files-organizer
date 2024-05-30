import os
import shutil
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get paths from environment variables
DOWNLOADS_FOLDER = os.getenv("DOWNLOADS_FOLDER")
DOCUMENTS_FOLDER = os.getenv("DOCUMENTS_FOLDER")
PICTURES_FOLDER = os.getenv("PICTURES_FOLDER")
VIDEOS_FOLDER = os.getenv("VIDEOS_FOLDER")

# Define file extensions and their corresponding folders
FILE_TYPES = {
    DOCUMENTS_FOLDER: [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    PICTURES_FOLDER: [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    VIDEOS_FOLDER: [".mp4", ".mov", ".avi", ".mkv"],
}

def organize_files(source_folder, file_types):
    """
    Organize files from the source folder into specified folders based on their file types.

    Parameters:
    source_folder (str): The folder where files are located to be organized.
    file_types (dict): A dictionary mapping target folders to lists of file extensions.
    """
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        
        if os.path.isfile(file_path):
            moved = False
            
            for target_folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    move_file(file_path, target_folder, filename)
                    moved = True
                    break
            
            if not moved:
                print(f"File '{filename}' remains in Downloads.")

def move_file(source_path, target_folder, filename):
    """
    Move a file to the target folder.

    Parameters:
    source_path (str): The current path of the file.
    target_folder (str): The destination folder for the file.
    filename (str): The name of the file.
    """
    target_path = os.path.join(target_folder, filename)
    shutil.move(source_path, target_path)

if __name__ == "__main__":
    organize_files(DOWNLOADS_FOLDER, FILE_TYPES)
    print("Files organized successfully.")
