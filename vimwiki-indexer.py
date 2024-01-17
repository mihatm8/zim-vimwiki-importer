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

# Function to create an index of wiki pages
def create_index(directory):
    index = []
    for folder, subfolder, files in os.walk(directory):
        for file_name in files:
            if Path(file_name).suffix == '.txt':
                stem = Path(file_name).stem
                if folder == './':
                    index.append(f'/{stem}')
                else:
                    index.append(f'{folder[1:]}/{stem}')
    index.sort()
    return index

# Function to append navigation to each page
def append_navigation(directory, index):
    navigation_str = '\\n'.join(index)
    for folder, subfolder, files in os.walk(directory):
        for file_name in files:
            file_path = Path(folder, file_name)
            try:
                with open(file_path, 'r+') as file:
                    content = file.read()
                    file.seek(0, 0)
                    file.write(navigation_str.rstrip('\\r\\n') + '\\n' + content)
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

# Generating and appending navigation
index = create_index(vimwiki_directory)
append_navigation(vimwiki_directory, index)
