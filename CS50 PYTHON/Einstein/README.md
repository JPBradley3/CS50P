# E=mc² Calculator

A Python Implementation of Einstein's Mass-Energy Equivalence Formula

## Overview

This Python script calculates the energy equivalent of a given mass using Einstein's famous equation E=mc². It demonstrates basic physics calculations, user input handling, and exponentiation in Python.

## The Physics

Einstein's mass-energy equivalence formula states:

- E = energy (in Joules)

- m = mass (in kilograms)

- c = speed of light in vacuum (approximately 299,792,458 m/s)

The script uses a simplified value of c = 300,000,000 m/s for calculation.

## Requirements

- Python 3.x

## Usage

### Running the Script

```

python emc2.py

```

### Example Sessions

```

Please input m as a mass in Kilograms(Kg): 1
90000000000000000

Please input m as a mass in Kilograms(Kg): 10
900000000000000000

Please input m as a mass in Kilograms(Kg): 0.001
90000000000000

```

## Code Explanation

### Variables

- c: Speed of light (300,000,000 m/s)

- m: Mass in kilograms (user input)

- e: Energy in Joules (calculated result)

### Complete Source Code

```python

## Starting code with known variables 'c' and 'm' and declaring them to be integers at the start to simplify.

c = int(300000000)
m = int(input("Please input m as a mass in Kilograms(Kg): "))

## Calculating for the "NEW VARIABLE" 'e' and then printing E=mc^2 as an integer result
e = m * c**2

print(e)

```

## Calculation Details

The script performs:

1. Sets c = 300,000,000 m/s

2. Gets mass input from user

3. Calculates e = m × c²

4. For c = 300,000,000: c² = 90,000,000,000,000,000

## Output Examples

- 1 kg → 90,000,000,000,000,000 J (90 petajoules)

- 0.001 kg (1 gram) → 90,000,000,000,000 J (90 terajoules)

- 1000 kg (1 metric ton) → 90,000,000,000,000,000,000 J (90 exajoules)

## Scientific Context

To put these numbers in perspective:

- 1 gram of matter = 90 TJ = energy of 21.5 kilotons of TNT

- The atomic bomb dropped on Hiroshima released ~63 TJ

- A kilogram of matter contains energy equivalent to ~21.5 megatons of TNT

## Limitations and Issues

### Current Limitations

1. Uses simplified speed of light (300,000,000 instead of 299,792,458 m/s)

2. Forces integer input (cannot handle decimal masses directly)

3. No input validation for negative numbers

4. No formatted output (scientific notation would be helpful)

### Accuracy Comparison

```

Simplified c = 300,000,000 m/s
Actual c = 299,792,458 m/s
Error = ~0.07%

```

## Improved Implementation

### With Proper Constants and Formatting

```python

# More accurate speed of light
c = 299792458  # m/s

# Accept decimal input
m = float(input("Please input mass in kilograms: "))

# Calculate energy
e = m * c**2

# Display with scientific notation
print(f"Mass: {m} kg")
print(f"Energy: {e:.2e} Joules")
print(f"Energy: {e:,.0f} Joules")

```

### With Input Validation

```python

def calculate_energy():
c = 299792458  # m/s

while True:
try:
m = float(input("Please input mass in kilograms: "))
if m < 0:
print("Mass must be positive!")
continue
break
except ValueError:
print("Please enter a valid number!")

e = m * c**2

# Display results
print(f"\nResults:")
print(f"Mass: {m} kg")
print(f"Speed of light: {c:,} m/s")
print(f"Energy: {e:.3e} Joules")

# Add context
tnt_equivalent = e / 4.184e9  # gigajoules per ton of TNT
print(f"TNT equivalent: {tnt_equivalent:.3e} tons")

calculate_energy()

```

## Educational Extensions

1. Compare energy content of common objects:

- Penny (2.5g): ~224 TJ

- AA battery (23g): ~2.06 PJ

- Human (70kg): ~6.3 EJ

2. Calculate reverse: How much mass for given energy?

3. Show relationship to nuclear reactions (mass defect)

4. Compare to daily energy consumption

## Testing Suggestions

Test with various inputs:

- Standard masses: 1, 10, 100 kg

- Small masses: 0.001, 0.000001 kg

- Large masses: 1000, 1000000 kg

- Edge cases: 0, negative numbers (should be handled)

- Non-numeric input: "abc", empty string

## Fun Facts

- Your body mass contains enough energy to power the entire United States for several days

- The mass-energy in a paperclip could power a city for weeks

- This equation explains how the sun produces energy through fusion
