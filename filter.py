import os
import shutil


def find_and_move_engine_files(folder_path, destination_folder, keyword="AF9"):
    """
    Parse through all .flac files in the folder, find files containing the given keyword,
    and move them to a new destination folder.

    :param folder_path: Path to the folder containing audio files
    :param destination_folder: Path to the folder where matching files will be moved
    :param keyword: Keyword to search for in the filename
    """
    matching_files = []

    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Iterate through all files in the folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a .flac file and contains the keyword
            if file.lower().endswith(".flac") and keyword in file:
                full_path = os.path.join(root, file)
                matching_files.append(full_path)

                # Move the file to the destination folder
                shutil.move(full_path, os.path.join(destination_folder, file))

    return matching_files


# Directly set the folder paths
folder_path = r"C:\Users\rachel.bennet\Desktop\Engine Noise Analysis Project\Audio\okAudio - 750"  # Replace with the source folder path
destination_folder = r"C:\Users\rachel.bennet\Desktop\Engine Noise Analysis Project\Audio\AF9 okAudio - 750"  # Replace with the destination folder path

# Example usage
if __name__ == "__main__":
    result = find_and_move_engine_files(folder_path, destination_folder)

    if result:
        print("Moved files:")
        for file in result:
            print(file)
    else:
        print(f"No .flac files containing 'AF9' found in {folder_path}.")
