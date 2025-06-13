# Fraction to Percentage Converter \\ \large Python Script


## Introduction

This Python program takes a user's input as a fraction (such as `3/4`) and converts it to a percentage, rounding up to the nearest whole number using Python's built-in `round` function. Special outputs are given for specific conditions: ``E'' (Empty) for 0 or `x/100`, and ``F'' (Full) when the fraction equals 1.

## Requirements

- Python 3.x

## Installation

Save the script to a file, for example `fraction_to_percent.py`, and ensure you have Python 3 installed.

## Usage

1. Open your terminal or command prompt.

2. Run the script using:

```

python fraction_to_percent.py

```

3. Follow the prompt and enter a fraction, e.g. `1/2`

4. The script will output the percentage, or ``E''/``F'' for empty/full.

## Example

**Input:**

```

What is your fraction: 2/3

```

**Output:**

```

67%

```

## Source Code

```python
def main():
fuel = float(get_fraction("What is your fraction:"))
print(f'{round(fuel * 100)}%')

def get_fraction(prompt):
while True:
try:
x = (input(prompt).split('/'))
if round(int(x[0]) / int(x[1]), 1) == 1:
print("F")
exit()
elif (int(x[0]) == 0) or (int(x[1]) == 100):
print("E")
exit()
elif (int(x[0]) < int(x[1])):
return float(x[0]) / float(x[1])
except (ValueError, ZeroDivisionError):
pass

main()
```

## Notes

- The script continues prompting until valid input is given.

- Division by zero and invalid formatting are handled gracefully.

- Full (1/1) and empty (0/x or x/100) cases yield ``F'' and ``E'' outputs.
