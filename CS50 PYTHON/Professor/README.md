# Arithmetic Quiz Game in Python


## Overview

This Python script is a command-line arithmetic quiz game designed to test and improve your mental addition skills. Users can select different difficulty levels and are presented with a series of random addition problems. Scores are displayed at the end.

## Requirements

- Python 3.x

- Only the `random` standard library module is required (`no` external dependencies).

## How to Run

1. Save the script as `quiz.py`.

2. Run the script from the command line:

```

python quiz.py

```

## Gameplay

1. [label=\arabic*.]

2. When prompted, select a difficulty level by entering `1`, `2`, or `3`:

- Level 1: Single-digit numbers (0--9).

- Level 2: Double-digit numbers (10--99).

- Level 3: Triple-digit numbers (100--999).

3. The program presents 10 addition problems based on the selected difficulty.

4. For each problem, you have **three** attempts to input the correct answer.

5. If your answer is incorrect, ``EEE'' is displayed.

6. After three incorrect attempts, the correct answer is shown, and the game moves to the next problem.

7. Your final score (number of correct answers on the first try) is displayed at the end.

## Script Structure

- `main():` Entry point. Handles the overall game flow.

- `get_level():` Prompts the user to select a valid difficulty level.

- `generate_integer(level):` Presents 10 random addition questions based on the chosen level, handles user input, counts correct answers, and displays the score.

## Example Session

```

Level: 2
34 + 47 = 81
56 + 13 = 67
EEE
56 + 13 = 69
EEE
56 + 13 = 68
EEE
56 + 13 = 69
56 + 13 = 69
...
Score: 1

```
