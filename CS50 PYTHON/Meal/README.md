# Meal Time Detector 

## Introduction

This Python script prompts the user to enter a time in 24-hour format (HH:MM) and prints which meal time it corresponds to: ``breakfast time'' (7:00-8:00), ``lunch time'' (12:00-13:00), or ``dinner time'' (18:00-19:00). If the provided time does not match any meal time, nothing is printed.

## Requirements

- Python 3.x

## Installation

No specific installation required. Save the script as `mealtime.py`.

## Usage

1. Open a terminal or command prompt.

2. Run the script with:

```

python mealtime.py

```

3. Enter a time in the `HH:MM` (24-hour) format when prompted.

4. The script will output the appropriate meal time if applicable.

## Examples

**Input:**

```

What time is it? 7:30

```

**Output:**

```

breakfast time

```

**Input:**

```

What time is it? 12:00

```

**Output:**

```

lunch time

```

**Input:**

```

What time is it? 18:59

```

**Output:**

```

dinner time

```

**Input:**

```

What time is it? 9:00

```

**Output:**

```

(no output)

```

## Source Code

```python
def main():
time = input("What time is it? ").strip()
if 7.0 <= convert(time) <= 8.0:
print("breakfast time")
elif 12.0 <= convert(time) <= 13.0:
print("lunch time")
elif 18.0 <= convert(time) <= 19.0:
print("dinner time")
else:
return

def convert(time):
x, y = time.split(":")
hr = float(x)
mins = float(y) * 1 / 60
return float(hr+mins)

if __name__ == "__main__":
main()
```

## Notes

- Only input in `HH:MM` 24-hour format will parse correctly.

- No output is printed if the time doesn't fall within meal intervals.

- Minutes are treated as a fractional hour, e.g., 7:30 is considered 7.5.
