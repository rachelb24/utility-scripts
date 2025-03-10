import json

def merge_json_files(file1_path, file2_path, output_path):
    """
    Merge two JSON files containing lists of objects and save the result to a new file.

    :param file1_path: Path to the first JSON file
    :param file2_path: Path to the second JSON file
    :param output_path: Path to save the merged JSON file
    """
    # Read the first file
    with open(file1_path, 'r') as file1:
        data1 = json.load(file1)

    # Read the second file
    with open(file2_path, 'r') as file2:
        data2 = json.load(file2)

    # Ensure both files contain lists
    if not isinstance(data1, list) or not isinstance(data2, list):
        raise ValueError("Both JSON files must contain lists.")

    # Merge the lists
    merged_data = data1 + data2

    # Save the merged data to a new file
    with open(output_path, 'w') as output_file:
        json.dump(merged_data, output_file, indent=4)

    print(f"Merged JSON saved to {output_path}")

# Example usage
file1_path = 'merged.json'
file2_path = 'filtered_engines4.json'
output_path = 'merged_NEW.json'

merge_json_files(file1_path, file2_path, output_path)
