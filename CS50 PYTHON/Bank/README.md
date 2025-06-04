# Greeting Price Calculator

A Python Script for Greeting-Based Pricing

## Overview

This Python script analyzes US English greetings and assigns prices based on the greeting type. It demonstrates string manipulation, conditional logic, and case-insensitive pattern matching.

## How It Works

The script assigns prices to greetings according to these rules:

- Greetings starting with "hello": \$0

- Greetings starting with "h" (but not "hello"): \$20

- All other greetings: \$100

## Requirements

- Python 3.x

## Usage

### Running the Script

Execute the script from the command line:

```

python greeting.py

```

### Example Sessions

```

Please type in a US English greeting: Hello
$0

Please type in a US English greeting: Hi
$20

Please type in a US English greeting: Good morning
$100

```

## Code Explanation

### Input Processing

1. Get user input with prompt "Please type in a US English greeting:"

2. Convert to lowercase for case-insensitive comparison

3. Strip whitespace from beginning and end

### Price Logic

- startswith("hello"): Checks if greeting begins with "hello"

- startswith("h"): Checks if greeting begins with "h"

- else: Catches all other greetings

### Complete Source Code

```python

## Get the users input as a greeting to compare later in the code
def main():
greeting = input("Please type in a US English greeting: ")

## Convert the greeting to be fair to capitalization
lowercase_greeting = greeting.lower()
stripped_answer = lowercase_greeting.strip()

## Match the users input to acceptable inputs and return an output as defined in the problem set
if stripped_answer.startswith(("hello")):
print("$0")
elif stripped_answer.startswith(("h")):
print("$20")
else:
print("$100")

```

## Key Features

- Case Insensitive: Works with "HELLO", "Hello", "hello", etc.

- Whitespace Handling: Strips leading and trailing spaces

- Simple Pricing Logic: Three-tier pricing system

- Clean Output: Displays price in dollar format

## Input Examples and Expected Output

- "Hello" → \$0

- "hello there" → \$0

- "HELLO WORLD" → \$0

- "Hi" → \$20

- "hey" → \$20

- "How are you?" → \$20

- "Good morning" → \$100

- "Greetings" → \$100

- "Bonjour" → \$100

## Code Improvements

### Current Issues

1. The main() function is defined but never called

2. Single parentheses in startswith() are unnecessary for single strings

### Suggested Fix

```

def main():
greeting = input("Please type in a US English greeting: ")

# Convert the greeting to be fair to capitalization
lowercase_greeting = greeting.lower()
stripped_answer = lowercase_greeting.strip()

# Match the users input to acceptable inputs
if stripped_answer.startswith("hello"):
print("$0")
elif stripped_answer.startswith("h"):
print("$20")
else:
print("$100")

if __name__ == "__main__":
main()

```

## Alternative Implementation

For more flexibility, consider using a dictionary approach:

```

def get_greeting_price(greeting):
greeting = greeting.lower().strip()

if greeting.startswith("hello"):
return 0
elif greeting.startswith("h"):
return 20
else:
return 100

def main():
greeting = input("Please type in a US English greeting: ")
price = get_greeting_price(greeting)
print(f"${price}")

if __name__ == "__main__":
main()

```

## Testing Considerations

- Test with various capitalizations

- Test with leading/trailing spaces

- Test edge cases like empty strings

- Test with non-English characters
