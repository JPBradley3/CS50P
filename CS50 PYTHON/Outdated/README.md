# Date Formatter 

## Introduction

This Python script prompts the user for a date (either in `Month Day, Year` or `MM/DD/YYYY` format), validates the input, and outputs the date in ISO format (`YYYY-MM-DD`). It supports various common date input styles.

## Requirements

- Python 3.x

## Installation

No installation is needed. Save the script as `date_formatter.py`.

## Usage

1. Run the script with:

```

python date_formatter.py

```

2. When prompted, enter a date in one of the supported formats:

- `Month Day, Year` (e.g., `March 9, 1999`)

- `MM/DD/YYYY` (e.g., `3/9/1999`)

3. The script will output the date in `YYYY-MM-DD` format.

## Examples

**Input:**

```

Date: March 9, 1999

```

**Output:**

```

1999-03-09

```

**Input:**

```

Date: 3/9/1999

```

**Output:**

```

1999-03-09

```

## Source Code

```python
def main():

months = [  # List containing months
"January", "February", "March", "April",
"May", "June", "July", "August",
"September", "October", "November", "December"
]

month = 0  # A variable that stores the index of the month
while True:
try:

# Gets user input, removes quotes and spaces on either side of the string
date = input("Date: ").replace('"', '').strip()

if date.count(" ") > 0:  # Checks if input is separated by a space
date = date.title().split(" ")

if date[1].count(',') > 0:  # Day followed by comma
date[1] = date[1].replace(',', '')
else:
continue  # Reprompt if not

# Check month and day are valid
if date[0] in months and 1 <= int(date[1]) <= 31:
month = months.index(date[0]) + 1
break

elif date.count("/") > 0:  # Checks if input is separated by '/'
date = date.split("/")

if 1 <= int(date[0]) <= 12 and 1 <= int(date[1]) <= 31:
month = int(date[0])
break

except ValueError:
continue

print(f'{date[2]}-{month:02d}-{int(date[1]):02d}')

main()
```

## Notes

- The script checks if the month and day are valid; otherwise, it will reprompt for input.

- Both full month names and numeric month input are accepted.

- Output is always in ISO format with zero-padded month and day.

- Only numeric input for day and a four-digit year are supported; invalid entries are ignored.
