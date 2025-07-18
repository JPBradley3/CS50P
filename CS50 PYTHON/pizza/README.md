# \textbf{CSV Menu Display Tool

*README Documentation*

*July 18, 2025*

\large A Python Script for Formatted CSV Display}

## Overview

This Python script provides a command-line utility to display CSV files as formatted tables. It reads a CSV file and presents its contents in a grid format using the tabulate library, making it ideal for displaying menu data or any tabular information in a readable format.

## Features

- Command-line interface for easy usage

- Automatic CSV file validation

- Grid-formatted table output

- Error handling for missing files and invalid formats

- Header row support

## Requirements

### Python Version

- Python 3.6 or higher

### Dependencies

- tabulate library

To install the required dependency:

```

pip install tabulate

```

## Installation

1. Clone or download the script to your local machine

2. Ensure Python 3.6+ is installed

3. Install the tabulate library using pip

## Usage

### Basic Syntax

```

python script.py filename.csv

```

### Example

```

python script.py menu.csv

```

### Arguments

- `filename.csv` - The path to the CSV file you want to display (required)

## Input File Format

The CSV file should follow standard CSV formatting:

- First row should contain column headers

- Subsequent rows contain data

- Values separated by commas

- Optional: Values can be quoted if they contain commas

### Example CSV Content

```

Item,Category,Price
Caesar Salad,Appetizers,$8.99
Grilled Salmon,Main Course,$24.99
Chocolate Cake,Desserts,$6.99

```

## Output Format

The script displays the CSV content in a grid table format:

- Clear column boundaries with grid lines

- Headers separated from data

- Aligned columns for better readability

## Error Handling

The script handles the following error cases:

- **Invalid number of arguments**: Displays usage instructions

- **Non-CSV file**: Reports that the file must be a CSV

- **File not found**: Reports missing file error

- **Other exceptions**: Displays the specific error message

## Functions

### `main()

`
Entry point of the script that:

- Validates command-line arguments

- Checks file extension

- Handles errors and calls the display function

### `print_csv_as_menu(menu)

`
Core function that:

- Opens and reads the CSV file

- Extracts headers and data

- Formats and prints the table using tabulate

## Example Output

Given a CSV file with menu items, the output would look like:

```

+----------------+-------------+---------+
| Item           | Category    | Price   |
+================+=============+=========+
| Caesar Salad   | Appetizers  | $8.99   |
+----------------+-------------+---------+
| Grilled Salmon | Main Course | $24.99  |
+----------------+-------------+---------+
| Chocolate Cake | Desserts    | $6.99   |
+----------------+-------------+---------+

```

## Limitations

- Large CSV files may take longer to process

- Terminal width may affect display of wide tables

- Special characters in CSV may require proper encoding

## Future Enhancements

Potential improvements could include:

- Support for different table formats (HTML, Markdown, etc.)

- Column width customization

- Filtering and sorting capabilities

- Support for multiple CSV files

- Export formatted output to file
