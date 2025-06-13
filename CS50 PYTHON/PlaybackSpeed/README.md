# Ellipsis String Formatter 

## Introduction

This Python script prompts the user for a short sentence and then replaces every space in the sentence with three dots (`...`). It demonstrates simple string manipulation and replacement.

## Requirements

- Python 3.x

## Installation

Save the script as `ellipsis_formatter.py`. No additional installation or library is required.

## Usage

1. Run the script using the command:

```

python ellipsis_formatter.py

```

2. Enter a sentence when prompted.

3. The script will print the sentence again, replacing each space with `...`

## Example

**Input:**

```

Please enter a short sentence: Hello world how are you

```

**Output:**

```

Hello...world...how...are...you

```

## Source Code

```python

## Get User Input Labeled as String
string = input("Please enter a short sentence: ")

## Find the spaces and repreint them with ...
new_string = string.replace(" " , "...")

## Print the new string
print(new_string)
```

## Notes

- All spaces in the user input are replaced, regardless of the number of spaces.

- The script does not modify any other punctuation or letters.
