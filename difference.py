import difflib
import os

def read_file(file_path):
    assert os.path.exists(file_path), f"File '{file_path}' not exists"

    # Read the file and return it like strings line
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def normalize_line(line):
    # Remove extra spaces and tabs at the edges of the line
    return line.strip()

def compare_files(file1_path, file2_path):
    file1_lines = read_file(file1_path)
    file2_lines = read_file(file2_path)

    normalized_file1_lines = [normalize_line(line) for line in file1_lines]
    normalized_file2_lines = [normalize_line(line) for line in file2_lines]

    # Create object of difflib class
    differ = difflib.Differ()
    diff = list()
    for line in differ.compare(normalized_file1_lines, normalized_file2_lines):
        if line[0] != ' ':
            diff.append(line)

    # Print differences
    print('\n'.join(diff))


if __name__ == "__main__":
    print("This script shows differences between two text files.")
    file1 = input("Path to first file: ")
    file2 = input("Path to second file: ")
    print("\nResult:")

    compare_files(file1, file2)
