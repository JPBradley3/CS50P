# Simple Expression Interpreter 

## Introduction

This Python script acts as a simple arithmetic interpreter. It prompts the user for an expression in the form "X OPERATOR Y" (for example: `3 + 5`), and outputs the result rounded to one decimal place. Supported operations are addition, subtraction, multiplication, and division.

## Requirements

- Python 3.x

## Installation

No installation is needed. Save the code as `interpreter.py`.

## Usage

1. Open a terminal or command prompt.

2. Run the script with:

```

python interpreter.py

```

3. Enter an arithmetic expression (with spaces between the numbers and the operator), such as `2 * 5`, when prompted.

4. The script will output the result to one decimal place.

## Examples

**Input:**

```

Expression: 2 + 3

```

**Output:**

```

5.0

```

**Input:**

```

Expression: 6 / 4

```

**Output:**

```

1.5

```

**Input:**

```

Expression: 9 - 1

```

**Output:**

```

8.0

```

## Source Code

```python
def interpreter():
expression = input("Expression: ").strip(" ")

value = expression.split(' ')

x = int(value[0])
y = value[1]
z = int(value[2])

if y == "+":
result = x + z
elif y == "-":
result = x - z
elif y == "*":
result = x * z
else:
result = x / z

print(f'{result:.1f}')

interpreter()
```

## Notes

- This script expects the expression to have spaces between operands and operator (e.g., `6 * 7`).

- Only integer operands are supported as written.

- Division is floating-point and all outputs are displayed to one decimal place.

- Invalid inputs will cause an exception.
