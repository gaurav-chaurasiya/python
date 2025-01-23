import os
import csv
from collections import defaultdict

def get_extension_counts_recursive(directory):
    # Dictionary to store the counts of each file extension for all folders
    folder_extension_counts = {}

    # Traverse the directory and its subdirectories
    for root, _, files in os.walk(directory):
        # Initialize a dictionary for the current folder
        extension_counts = defaultdict(int)

        for file in files:
            # Get the file extension
            ext = os.path.splitext(file)[-1].lower()
            extension_counts[ext] += 1

        # Sort extensions by count in descending order and save the sorted counts for the current folder
        folder_extension_counts[root] = dict(sorted(extension_counts.items(), key=lambda x: x[1], reverse=True))

    return folder_extension_counts

def write_extension_counts_to_csv(folder_extension_counts, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(['Folder', 'Extension', 'Count'])
        
        # Write data for each folder
        for folder, extension_counts in folder_extension_counts.items():
            for ext, count in extension_counts.items():
                if ext:  # Ignore files with no extension
                    writer.writerow([folder, ext, count])

if __name__ == "__main__":
    # Specify the directory to scan
    directory = input("Enter the directory path to scan: ").strip()

    if not os.path.exists(directory):
        print("The specified directory does not exist!")
    else:
        # Get extension counts recursively
        folder_extension_counts = get_extension_counts_recursive(directory)

        # Specify the output CSV file
        output_file = 'extension_counts.csv'

        # Write the results to the CSV file
        write_extension_counts_to_csv(folder_extension_counts, output_file)

        print(f"Extension counts have been written to {output_file}")
