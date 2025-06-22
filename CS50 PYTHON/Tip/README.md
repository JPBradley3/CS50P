# Meal Tip Calculator


## Overview

This Python script computes the tip based on the cost of a meal and the desired tip percentage. The user is prompted for both values, and the tip amount is calculated and formatted to two decimal places.

## Requirements

- Python 3.x

- No external dependencies are required.

## How to Run

1. Save the script as `tip.py`.

2. Run the script:

```

python tip.py

```

## Usage

1. When prompted, enter the cost of the meal (you may use decimals, e.g., `50.5`).

2. When prompted, enter the tip percentage (just the number, such as `15` for 15%).

3. The script will print out the tip amount rounded and formatted to two decimal places.

## Example Session

```

How much was the meal? 50
What percentage would you like to tip? 15
Leave $7.50

```

## How it Works

- `dollars_to_float(d)`: Takes the meal input as a string and converts it to a float.

- `percent_to_float(p)`: Takes the tip percentage input as a string and converts it to a float.

- The tip is calculated by multiplying the cost (`dollars`) by the percentage (`percent/100`).

- The result is displayed using Python string formatting for two decimal places.

## Notes

- Input validation is minimal; entering non-numeric values will cause an error.

- Percentages should be entered as numbers only (e.g., `15`).
