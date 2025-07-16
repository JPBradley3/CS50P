# Python Line Counter


## Introduction

This Python script counts the number of non-comment, non-empty lines in a Python file. It's designed to be used from the command line and follows specific error handling guidelines.

## Features

- Counts only lines that contain actual code (ignores comments and whitespace)

- Command line interface

- Comprehensive error handling

- Verifies that input file has .py extension

## Usage

The script should be run from the command line with exactly one argument - the path to the Python file to analyze:

```
python lines.py myfile.py
```

## Error Handling

The script handles the following error conditions:

- Too few command-line arguments

- Too many command-line arguments

- Input file is not a Python file (doesn't end with .py)

- Input file does not exist

## Code Overview

The script consists of three main components:

### Main Function

The main function validates command-line arguments and calls the appropriate functions.

```python
def main():
if len(sys.argv) < 2:
sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
sys.exit("Too many command-line arguments")
else:
if not sys.argv[1].endswith(".py"):
sys.exit("Not a python file")
else:
print(read_data(sys.argv[1]))
```

### Read Data Function

This function reads the input file and counts lines that are not comments or whitespace.

```python
def read_data(filename):
try:
with open(filename, 'r') as file:
lines = file.readlines()

count = 0
for line in lines:
stripped = line.strip()
if stripped and not stripped.startswith("#"):
count += 1
return count
except FileNotFoundError:
sys.exit("File does not exist")
```

### Script Execution

The script checks if it's being run directly and calls the main function.

```python
if __name__ == "__main__":
main()
```

## Requirements

- Python 3.x

- No external dependencies beyond the standard library

## License

This project is licensed under the MIT License - see the LICENSE file for details.
