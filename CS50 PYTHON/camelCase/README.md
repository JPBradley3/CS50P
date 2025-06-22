# CamelCase to snake\_case Converter Script


## Overview

This Python script converts a given string in `camelCase` format to `snake_case` format. It is useful for renaming files, variables, or other identifiers to follow the snake_case naming convention.

## Requirements

- Python 3.x

- No external packages are required.

## How to Run

1. Save the script as `camel2snake.py`.

2. Run the program in your terminal:

```

python camel2snake.py

```

## Usage

1. When prompted, input a file name or identifier in camelCase.

2. The script prints the corresponding snake_case version on the same line.

## Example Session

```

Please enter the camel case file name: modelPlaygroundTest
snake_case: model_playground_test

```

## Script Description

- The user is prompted to input a name in camelCase.

- The script iterates through each character:
\begin{itemize}

- Lowercase letters are printed as-is.

- Each uppercase letter is preceded by an underscore and printed in lowercase.

\end{itemize}

## Limitations

- Special characters and numbers are not specifically handled.

- An initial uppercase letter will result in an initial underscore (e.g., ``OutlierTest'' $\rightarrow$ ``_outlier_test'').
