# License Plate Validity Checker 

## Introduction

This Python script checks whether a user-provided license plate string is valid according to specific rules:

- Plate length must be between 2 and 6 characters.

- If any digits are present, they must only appear as the last one or two characters.

- The first occurrence of a digit must not be a ``0'' if the number is two digits long.

After evaluating, the script prints ``Valid'' or ``Invalid''.

## Requirements

- Python 3.x

## Installation

Save the script as `plate_checker.py`.

## Usage

1. Run the script:

```

python plate_checker.py

```

2. Enter a license plate string when prompted.

3. The script will output either ``Valid'' or ``Invalid''.

## Examples

**Input:**

```

Plate: AB123

```

**Output:**

```

Valid

```

**Input:**

```

Plate: ABC045

```

**Output:**

```

Invalid

```

**Input:**

```

Plate: A1B234

```

**Output:**

```

Invalid

```

**Input:**

```

Plate: AB

```

**Output:**

```

Valid

```

## Source Code

```python

# Program checks if a plate is valid
def main():
plate = input("Plate: ")  # Prompts user for plate number

if is_valid(plate):
print("Valid")
else:
print("Invalid")

def is_valid(s):

# If plate number is not within the range of 2 and 6, it returns false
if not (2 <= len(s) <= 6):
return False

# If plate number is within the range
for i in range(len(s)):

# Checks if plate number has digits
if s[i].isdigit():

# If the first digit that occurred is 0
if i == len(s) - 2 and s[i] == '0':
return False

# If digit occurs in a position outside the last two characters
elif not (i == len(s) - 1 or i == len(s) - 2):
return False
return True

main()
```

## Notes

- Input is case-sensitive.

- Only digit placement is validated; letters are not specifically checked.

- There is no external library dependency.
