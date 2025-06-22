# Vowel Remover Script


## Overview

This Python script removes all vowels (both uppercase and lowercase) from a given input string. The program prompts the user to enter text and then prints the same text with all vowels omitted.

## Requirements

- Python 3.x

- No external packages.

## How to Run

1. Save the script as `remove_vowels.py`.

2. Run it using:

```

python remove_vowels.py

```

## Usage

1. When prompted, enter any string.

2. The script will display the same string with all vowels (a, e, i, o, u, both lowercase and uppercase) removed from it.

## Example Session

```

Input: Outlier Model Playground
Output: tlr Mdl Plygrnd

```

## Script Description

- The main function collects user input and constructs an output string by skipping over vowels, using the helper function `isnotvowel`.

- The `isnotvowel` function checks if a given character is not a vowel (case-insensitive).

- All non-vowel characters are concatenated to the output and displayed.
