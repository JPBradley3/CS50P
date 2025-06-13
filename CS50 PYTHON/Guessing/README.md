# Number Guessing Game 

## Introduction

This simple Python program is a "Number Guessing Game." The user is prompted to select a positive upper limit for the guessing range (`Level`), and the computer generates a random secret number between 1 and this level (inclusive). The user then guesses the number, receiving feedback if their guess is too small or too large, until they guess correctly.

## Requirements

- Python 3.x

## Installation

No installation is required. Save the script into a file, e.g., `guessing_game.py`.

## Usage

1. Run the script with the command:

```

python guessing_game.py

```

2. Enter a positive integer at the "Level:" prompt to set the upper bound.

3. At the "Guess:" prompt, enter guesses until the correct number is found.

## Example

**Session Example:**

```

Level: 10
Guess: 5
Too small!
Guess: 8
Too large!
Guess: 7
Just Right!

```

## Source Code

```python
import random

while True:
try:
i = int(input("Level: "))
if i > 0:
break
except:
pass

r = random.randint(1,i)

while True:
try:
a = int(input("Guess: "))
if a != 0:
if a < r:
print("Too small!")
elif a > r:
print("Too large!")
else:
print("Just Right!")
break
except:
pass
```

## Notes

- The script ignores invalid or non-positive inputs for the upper limit.

- The guessing loop will not accept '0' as a valid guess.

- Errors from non-integer input or other exceptions are silently ignored.
