# Python ASCII Art with \texttt{pyfiglet


## Overview

This Python script uses the `pyfiglet` library to create stylized ASCII art text. Users may optionally specify a font via command-line arguments; if no font is given, the script selects one at random.

## Code

```python
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet.getFonts()

if len(sys.argv) == 1:
is_random = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
is_random = False
else:
print("Invalid Usage")
sys.exit(1)

if is_random == False:
try:
figlet.setFont(font=sys.argv[2])
except:
print("Invalid usage")
sys.exit(1)
else:
font = random.choice(figlet.getFonts())

text = input("Input:")
print("Output:", figlet.renderText(text))
```

## How It Works

1. Imports the necessary libraries (`pyfiglet`, `sys`, `random`).

2. Checks command-line arguments:

- If no arguments: chooses a random font.

- If `-f <fontname>` or `--font <fontname>`: uses the specified font.

- Otherwise, prints ``Invalid Usage'' and exits.

3. Asks the user for input text.

4. Prints the ASCII art version of the input text using the chosen font.

## Requirements

- Python 3.x

- `pyfiglet` (`pip install pyfiglet`)

## Example Usage

```

$ python script.py
Input: Hello
Output:  # Random font ASCII art for 'Hello'

$ python script.py -f slant
Input: Outlier
Output:  # 'Outlier' rendered in 'slant' font

```

## Notes

- You can see available font names using `pyfiglet.Figlet().getFonts()`.

- To use a specific font, run: `python script.py -f <fontname>` or `python script.py --font <fontname>`.

- The script will exit with an error if invalid usage is detected.

- For full documentation, see: <https://github.com/pwaller/pyfiglet>
