# CSV Name Splitter

## Overview

This script reads an input CSV file containing student names and house information, splits the `name` field (assumed to be in ``Last, First'' format) into separate `first` and `last` columns, and writes the result to a new CSV file.

## Usage

Run the script from the command line with two arguments:

```

python script.py input.csv output.csv

```

Here, `input.csv` is the original file, and `output.csv` is the desired output file.

## Requirements

- Python 3.x

- The input CSV must contain a ``name'' field in ``Last, First'' format, and a ``house'' field.

## Input Format

An example row of the input CSV:

```

name,house
Potter, Harry,Gryffindor

```

## Output Format

The output CSV will have the following headers:

```

first,last,house
Harry,Potter,Gryffindor

```

## Error Handling

- The script checks whether both input and output filenames are provided.

- Only files with the `.csv` extension are accepted.

- If the input file does not exist, or another error occurs, a message will be displayed and the script will exit.
