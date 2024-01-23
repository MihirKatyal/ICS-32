import os
import sys

def list_directory(path, options):
    files = []
    for root, dirs, filenames in os.walk(path):
        if '-f' in options:
            # Output only files
            files.extend([os.path.join(root, filename) for filename in filenames])
        else:
            # Output files and directories
            files.extend([os.path.join(root, filename) for filename in filenames])
            if '-r' not in options:
                break  # If not recursive, only list the current directory

    if '-s' in options:
        # Filter by file name
        files = [file for file in files if options['-s'] in os.path.basename(file)]

    if '-e' in options:
        # Filter by file extension
        files = [file for file in files if file.endswith(options['-e'])]
