# README for Minutes Lived Script

## Overview

This script prompts the user to input their date of birth (DOB) in the format `YYYY-MM-DD`. It then calculates the number of minutes the user has lived up to today and prints this value in words. For example, an output might be *``Twelve million three hundred forty-five thousand six hundred seventy-eight minutes''*. If the input is not in the correct format, the script exits with an error.

## Requirements

This script requires Python 3 and the following Python packages:

- inflect (`pip install inflect`)

## How to Use

1. Ensure you have Python 3 installed on your system.

2. Install the required package `inflect`:

```

pip install inflect

```

3. Save the script as `minutes_lived.py`.

4. Run the script in your terminal:

```

python minutes_lived.py

```

5. When prompted, enter your date of birth in the `YYYY-MM-DD` format (e.g., `1990-04-23`).

6. The script will print the number of minutes you have lived, in words (e.g., ``Seventeen million five hundred thousand minutes'').

## Script Structure

- **main()**: Prompts for DOB, validates input, processes the calculation, and prints the result.

- **check_valid(s)**: Returns True if `s` matches the required date format; otherwise, returns False.

- **return_diff(i)**: Takes a DOB string, computes the difference in minutes between the input date and today, and returns the count in words.

## Function Descriptions

\begin{description}
\item[`main()`] Main entry point. Handles user input, calls validation and conversion functions, and formats output.
\item[`check_valid(s)`] Uses a regular expression to check if the input string `s` has the format `YYYY-MM-DD`. Returns `True` if valid, otherwise `False`.
\item[`return_diff(i)`] Converts the input date string `i` to a timestamp, determines today's timestamp, calculates the minutes difference, and uses the `inflect` module to express the result in words.
\end{description}

## Example Usage

```

$ python minutes_lived.py
Date of Birth: 2000-01-01
Twelve million one hundred thirty-eight thousand four hundred forty minutes

```

## Notes

- The script expects the input date to be in the exact `YYYY-MM-DD` format. Invalid input will cause the script to exit.

- The output is capitalized and prints the number of minutes in words, followed by the word `minutes`.

- Leap years and day boundaries are handled via Python's `datetime` module.

