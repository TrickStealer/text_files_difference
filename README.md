# text_files_difference
Script to show difference between two files.

<br/>

**Includes files:**

| File                | Description                                                  |
| ------------------- | ------------------------------------------------------------ |
| difference.py       | File with code of the script                                 |
| 1. json <br/>2.json | Example files with simple json code to check how script works. They have only one difference in value of key "age" and in count of spaces ahead of line |

<br/>

**Usage:**

1. Launch script **difference.py** using terminal. Add arguments with paths to files. For example enter:
   ```bash
   python difference.py 1.json 2.json
   ```
2. Script should show only lines with differences. Except differences in whitespace characters from the beginning and end of each line.

