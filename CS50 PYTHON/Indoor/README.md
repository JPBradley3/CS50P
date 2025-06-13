# Lowercase Converter

## Introduction

This simple Python script prompts the user to enter a sentence in all capital letters and then prints out the same sentence in all lowercase. It demonstrates how to easily convert a string to lowercase using Python.

## Requirements

- Python 3.x

## Installation

No installation is necessary. Save the script to a file, e.g., `lowercase_converter.py`.

## Usage

1. Open a terminal or command prompt.

2. Run the script with:

```

python lowercase_converter.py

```

3. When prompted, type a sentence (ideally in all capital letters).

4. The script will output the same sentence in all lowercase letters.

## Example

**Input:**

```

Yell something in all caps!!!: HELLO, WORLD!

```

**Output:**

```

hello, world!

```

## Source Code

```python
string = input("Yell something in all caps!!!: ")
lowercase_string = string.lower()
print(lowercase_string)
```

## Notes

- The script converts **all** user input to lowercase, regardless of the original casing.

- The input does not have to be in uppercase, but that's the purpose for demonstration.
