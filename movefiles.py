import json
import os
import shutil

def move_filtered_audio_files(filtered_json, ok_folder, nok_folder, dest_ok_folder, dest_nok_folder, output_file):
    try:
        # Load filtered JSON data
        with open(filtered_json, 'r') as f:
            data = json.load(f)

        # Extract engine numbers from filtered JSON
        engine_numbers = {item["engineNo"] for item in data}

        # Ensure destination folders exist
        os.makedirs(dest_ok_folder, exist_ok=True)
        os.makedirs(dest_nok_folder, exist_ok=True)

        # Search for matching files in OK and NOK folders
        moved_files = []

        folder_mappings = {
            ok_folder: (dest_ok_folder, "OK"),
            nok_folder: (dest_nok_folder, "NOK")
        }

        for source_folder, (destination_folder, status) in folder_mappings.items():
            if not os.path.exists(source_folder):
                print(f"Warning: Folder '{source_folder}' not found. Skipping...")
                continue

            for file_name in os.listdir(source_folder):
                for engine_no in engine_numbers:
                    if engine_no in file_name:
                        src_path = os.path.join(source_folder, file_name)
                        dest_path = os.path.join(destination_folder, file_name)

                        # Move the file to the appropriate destination folder
                        shutil.move(src_path, dest_path)

                        # Store moved file info
                        moved_files.append({
                            "engineNo": engine_no,
                            "originalPath": src_path,
                            "newPath": dest_path,
                            "folder": status
                        })
                        print(f"Moved: {file_name} -> {dest_path}")

        # Save results to output JSON file
        with open(output_file, 'w') as f:
            json.dump(moved_files, f, indent=4)

        print(f"Filtered and moved files saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
filtered_json = "filtered.json"        # JSON file containing filtered engine numbers
ok_folder = r'C:\Users\rachel.bennet\Desktop\Engine Noise Analysis Project\Audio\okAudio'  # Path to the source OK folder
nok_folder = r'C:\Users\rachel.bennet\Desktop\Engine Noise Analysis Project\Audio\AF9 - NOK - To filter final'  # Path to the source NOK folder

# Updated destination folders
dest_ok_folder = r'C:\Users\rachel.bennet\Desktop\Engine Noise Analysis Project\Audio\okwnoise'  # Destination folder for OK files
dest_nok_folder = r'C:\Users\rachel.bennet\Desktop\Engine Noise Analysis Project\Audio\NOKwNoise - ALL'  # Destination folder for NOK files

output_file = "moved_files.json"  # Output JSON file to store moved file details

move_filtered_audio_files(filtered_json, ok_folder, nok_folder, dest_ok_folder, dest_nok_folder, output_file)
