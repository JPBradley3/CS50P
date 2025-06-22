# Restaurant Menu Order Calculator


## Overview

This Python script implements an interactive order calculator for a restaurant menu. Users can enter various menu items to add them to their bill, and the program keeps and displays a running total. Input ends when an invalid item is entered or when the `CTRL+D` shortcut (EOF) is encountered.

## Requirements

- Python 3.x

- No external libraries are required.

## How to Run

1. Save the script as `menu.py`.

2. Run from your terminal or command line:

```

python menu.py

```

## Usage

1. You will be prompted to enter an item name from the menu.

2. Each valid item (case-insensitive) adds its price to the total and prints the updated amount.

3. Enter an invalid item name or press `CTRL+D` (or `CMD+D` on Mac) to exit.

## Menu

\begin{tabular}{ll}

**Item** & **Price**

\hline
Baja Taco            & \$4.25
Burrito              & \$7.50
Bowl                 & \$8.50
Nachos               & \$11.00
Quesadilla           & \$8.50
Super Burrito        & \$8.50
Super Quesadilla     & \$9.50
Taco                 & \$3.00
Tortilla Salad       & \$8.00
\end{tabular}

## Example Session

```

Item: taco
Total: $3.00
Item: burrito
Total: $10.50
Item: nachos
Total: $21.50
Item: pizza

```

## Functionality

- The menu is stored in a Python dictionary mapping items to prices.

- User input is normalized (with `.title()`) so that case and minor style differences are handled.

- The total price is displayed after each valid item.

- Any input not matching a menu item ends the program.

- Pressing `CTRL+D` triggers a graceful exit.
