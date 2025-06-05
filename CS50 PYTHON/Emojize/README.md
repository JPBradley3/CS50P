# Emoji Alias Conversion in Python

## Overview

This Python script provides a minimal interface for converting emoji aliases (`:smile:`, `:heart:`, etc.) into their corresponding Unicode emoji, using the `emoji` package. The interface reads user input, processes it, and outputs the resulting text with emojis rendered.

## Code

```python
from emoji import emojize

x = input("EInput: ")
print("Output:", emojize(x, language="alias"))
```

## How It Works

1. The script prompts the user to input a string possibly containing emoji aliases (such as `:smile:`).

2. The `emojize` function is called with `language="alias"` to ensure that the aliases within the string are replaced with their emoji equivalents.

3. The processed output is printed to the console.

## Requirements

- Python 3.x

- The `emoji` library (install via `pip install emoji`)

## Example Usage

```

EInput: I love Python! :snake: :heart:
Output: I love Python! 🐍 ❤️

```

## Notes

- For a full list of supported aliases, see the `emoji` documentation: <https://github.com/carpedm20/emoji>

- The code is kept minimal and Pythonic, relying only on the necessary functions and idioms.
