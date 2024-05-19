import os

def parse_structure(lines):
    """
    Parse the directory structure from the given lines.

    Args:
        lines (list): List of lines representing the directory structure.

    Returns:
        tuple: Root directory, list of directories, and list of files.
    """
    directories = []
    files = []
    path_stack = []

    # Extract the first element as the root directory
    root_dir = lines.pop(0).strip()
    if root_dir.endswith('/') or '.' in root_dir:
        raise ValueError("The first element must be the root directory name without '/' or extension.")

    for line in lines:
        if not line.strip():
            continue  # Skip empty lines
        # Calculate the indentation level by counting the number of '│' characters
        indent_level = line.count('│')

        # Clean the line to get the file or directory name
        clean_line = line.strip().split('├── ')[-1].split('└── ')[-1].rstrip('/')

        # Adjust the path stack according to the indentation level
        while len(path_stack) > indent_level:
            path_stack.pop()
        
        current_path = os.path.join(root_dir, *path_stack, clean_line)

        if line.strip().endswith('/'):
            # It's a directory
            directories.append(current_path)
            path_stack.append(clean_line)
        else:
            # It's a file
            files.append(current_path)

    return root_dir, directories, files

def create_directory_structure(root_dir, directories):
    """
    Create the directory structure.

    Args:
        root_dir (str): The root directory.
        directories (list): List of directories to create.
    """
    # Create the root directory
    os.makedirs(root_dir, exist_ok=True)
    print(f"Root directory created: {root_dir}")

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory created: {directory}")

def create_files(files):
    """
    Create the files.

    Args:
        files (list): List of file paths to create.
    """
    for file_path in files:
        directory = os.path.dirname(file_path)
        os.makedirs(directory, exist_ok=True)
        open(file_path, 'a').close()
        print(f"File created: {file_path}")

def save_paths_to_file(paths, file_name):
    """
    Save the paths to a file.

    Args:
        paths (list): List of paths to save.
        file_name (str): The name of the file to save the paths in.
    """
    with open(file_name, 'w') as file:
        file.write('\n'.join(paths))
    print(f"Paths saved to file: {file_name}")

# Path to the "structure.txt" file
structure_file = "structure.txt"

# Check if the "structure.txt" file exists
if not os.path.exists(structure_file):
    print(f"The file '{structure_file}' does not exist.")
    exit(1)

# Read the content of the "structure.txt" file
with open(structure_file, 'r') as file:
    lines = file.readlines()

# Parse the directory structure
root_dir, directories, files = parse_structure(lines)

# Save the directory paths to a file
save_paths_to_file(directories, "directories.txt")

# Save the file paths to a file
save_paths_to_file(files, "files.txt")

# Create the directory structure
create_directory_structure(root_dir, directories)

# Create the files
create_files(files)
