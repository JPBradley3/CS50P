# Fruit Calories Lookup 

## Introduction

This Python script prompts the user to enter the name of a fruit. If the fruit is in a predefined list, the script outputs the corresponding number of calories. Input is case-insensitive.

## Requirements

- Python 3.x

## Installation

No installation is necessary. Save the script as `fruit_calories.py`.

## Usage

1. Run the script with:

```

python fruit_calories.py

```

2. When prompted (`Item:`), type the name of a fruit (e.g., `apple`).

3. If the fruit is known, the script prints its calorie count.

## Examples

**Input:**

```

Item: banana

```

**Output:**

```

110

```

**Input:**

```

Item: honeydew melon

```

**Output:**

```

50

```

**Input:**

```

Item: mango

```

**Output:**

```

(no output)

```

## Source Code

```python

# Program prompts user for fruit as input and outputs amount of calories
def main():
food = input("Item: ").lower()  # Prompts user for string input and converts all characters to lowercase

food_items = [   # List of dictionaries containing name of fruit and it's amount of calories
{'fruit': 'apple', 'calories': 130},
{'fruit': 'avocado', 'calories': 50},
{'fruit': 'banana', 'calories': 110},
{'fruit': 'cantaloupe', 'calories': 50},
{'fruit': 'grapefruit', 'calories': 60},
{'fruit': 'grapes', 'calories': 90},
{'fruit': 'honeydew melon', 'calories': 50},
{'fruit': 'kiwifruit', 'calories': 90},
{'fruit': 'lemon', 'calories': 15},
{'fruit': 'lime', 'calories': 20},
{'fruit': 'nectarine', 'calories': 60},
{'fruit': 'orange', 'calories': 80},
{'fruit': 'peach', 'calories': 60},
{'fruit': 'pear', 'calories': 100},
{'fruit': 'pineapple', 'calories': 50},
{'fruit': 'plums', 'calories': 70},
{'fruit': 'strawberries', 'calories': 50},
{'fruit': 'sweet cherries', 'calories': 100},
{'fruit': 'tangerine', 'calories': 50},
{'fruit': 'watermelon', 'calories': 80}
]

for item in food_items:

# Checks if user input is a fruit name on the list
if item["fruit"] == food:
print(item["calories"])  # Prints amount of calories

main()
```

## Notes

- The input is case-insensitive.

- If the fruit is not found, there is no output.

- Only the listed fruits will return a result.
