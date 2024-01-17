import os, pprint
from pathlib import Path

def get_directory_input(prompt):
    while True:
        directory = input(prompt)
        if os.path.isdir(directory):
            return directory
        else:
            print("Invalid directory, please try again.")

# Ask user for the VimWiki directory
vimwiki_directory = get_directory_input('Enter the path to your VimWiki directory: ')
os.chdir(vimwiki_directory)

# Function to process files in the directory
def process_files(directory):
    for folder, subfolder, files in os.walk(directory):
        pprint.pprint(folder)  # Print the current folder being processed
        for file_name in files:
            file_path = Path(folder, file_name)
            try:
                with open(file_path, 'r') as file:
                    original_content = file.readlines()
                with open(file_path, 'w') as file:
                    # Remove the first four lines from the file
                    file.write(''.join(original_content[4:]))
                # Create a link format string for each file
                stem = Path(file_name).stem
                link_format = '[[./{}/{}|{}]]\\n'.format(Path(folder).name, stem, stem)
                # Optionally print the link format (can be used for debugging or verification)
                # print(link_format)
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

# Call the function to process files
process_files(vimwiki_directory)
