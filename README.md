# 📂 Directory Structure Parser 📂

This Python project analyzes a textual representation of a directory structure to extract the paths of files and directories. It saves these paths into separate files for directories and files respectively. Finally, it utilizes the saved paths to recreate the original directory structure on the file system.

## ✨ Features ✨

- 📄 **Parses a text representation of a directory structure**
- 🔍 **Extracts file and directory paths from the textual representation**
- 📁 **Saves directory paths to a file named "directories.txt"**
- 📄 **Saves file paths to a file named "files.txt"**
- 🌳 **Recreates the original directory structure on the file system based on the saved paths**

# 📋 Requirements 📋

- 🐍 **Python 3.x**
- 📂 **os module (included in Python standard library)**

🚀 Usage 🚀

1. Prepare a text file named "structure.txt" that represents the directory structure using the following format:

```bash
 root_directory
 │
 ├── directory1/
 │   ├── subdirectory1/
 │   │   └── file1.txt
 │   └── file2.txt
 │
 ├── directory2/
 │   └── file3.txt
 │
 └── file4.txt
```

2. Place the "structure.txt" file in the same directory as the Python script.
3. Run the Python script:

```bash
python3 directory_structure_parser.py
```

4. The script will parse the "structure.txt" file, extract the file and directory paths, and save them to "directories.txt" and "files.txt" respectively.
5. The script will then use the saved paths to recreate the original directory structure on the file system.
6. The created directories and files will be displayed in the console output.

# 📂 File Structure

 - directory_structure_parser.py: The main Python script that parses the directory structure and recreates it on the file system.
 - structure.txt: The input file containing the textual representation of the directory structure.
 - directories.txt: The output file containing the extracted directory paths.
 - files.txt: The output file containing the extracted file paths.

# 🔧 Functions

 - parse_structure(lines): Parses the directory structure from the given lines and returns the root directory, list of directories, and list of files.
 - create_directory_structure(root_dir, directories): Creates the directory structure based on the root directory and the list of directories.
 - create_files(files): Creates the files based on the list of file paths.
 - save_paths_to_file(paths, file_name): Saves the given paths to a file with the specified file name.

# ⚠️ Error Handling

- If the "structure.txt" file does not exist, an error message will be displayed, and the script will exit.
- If the first element in the "structure.txt" file is not a valid root directory name (contains '/' or '.'), a ValueError will be raised.

# 📝 Example

Given the following "structure.txt" file:

```bash
project
│
├── src/
│   ├── main.py
│   └── utils/
│       └── helper.py
│
├── docs/
│   └── README.md
│
└── data/
    ├── input.csv
    └── output.txt
```

Running the script will generate the following output:

```bash
Paths saved to file: directories.txt
Paths saved to file: files.txt
Root directory created: project
Directory created: project/src
Directory created: project/src/utils
Directory created: project/docs
Directory created: project/data
File created: project/src/main.py
File created: project/src/utils/helper.py
File created: project/docs/README.md
File created: project/data/input.csv
File created: project/data/output.txt
```

The resulting directory structure will be created on the file system.

# 📜 License

This project is open-source and available under the MIT License.

# 🤝 Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
