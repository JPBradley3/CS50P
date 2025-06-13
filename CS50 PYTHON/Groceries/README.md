# Grocery List Counter

## Introduction

This Python program allows users to build an inventory of grocery items by entering them line-by-line. Items are entered in any order and are case-insensitive. Upon pressing `Ctrl-D` (on macOS/Linux) or `Ctrl-Z` (on Windows), the input ends, and the program prints a sorted list of all items with their quantities, one per line.

## Requirements

- Python 3.x

## Installation

No installation required. Simply save the code to a file, e.g., `grocery_counter.py`.

## Usage

1. Run the script with:

```

python grocery_counter.py

```

2. Type one grocery item per line. Press `Ctrl-D` (macOS/Linux) or `Ctrl-Z` (Windows) to finish input and display the results.

## Example

**Input:**

```

apple
banana
Apple
BANANA
banana
^D  # or ^Z on Windows

```

**Output:**

```

2 APPLE
3 BANANA

```

## Source Code

```python
def main():
grocery_list = {}
while True:
try:
item = input().upper()
if item in grocery_list:
grocery_list[item] += 1
else:
grocery_list[item] = 1
except EOFError:
for item in sorted(grocery_list):
print(grocery_list[item], item)
break

main()
```

## Notes

- Item names are stored in upper case for case insensitivity.

- Items are output in alphabetical order.

- To finish entering items, use the EOF command for your operating system.
