import difflib
import os
import argparse

def read_terminal():
    parser = argparse.ArgumentParser(description='Differences between two text files')

    parser.add_argument('file1', type = str, help = 'Path to first file')
    parser.add_argument('file2', type = str, help = 'Path to second file')

    args = parser.parse_args()

    file1 = args.file1
    file2 = args.file2

    return file1, file2

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
    print("\nResult:")
    print('\n'.join(diff))


if __name__ == "__main__":
    file1, file2 = read_terminal()
    compare_files(file1, file2)
