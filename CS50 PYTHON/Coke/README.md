# Coin Machine Simulator

A Python Script for Simulating Coin-Operated Transactions

## Overview

This Python script simulates a coin-operated machine that accepts specific coin denominations (5, 10, and 25 cents) until the required amount of 50 cents is reached. It demonstrates input validation, running totals, and change calculation.

## How It Works

1. The machine requires 50 cents to complete a transaction

2. Only accepts coins of 5, 10, or 25 cents

3. Displays remaining amount due after each coin

4. Calculates and returns change if overpayment occurs

## Requirements

- Python 3.x

## Usage

### Running the Script

```

python coin_machine.py

```

### Example Session

```

Insert Coin: 25
Amount Due: 25
Insert Coin: 10
Amount Due: 15
Insert Coin: 10
Amount Due: 5
Insert Coin: 5
Amount Due: 0
Change Owed: 0

```

### Example with Change

```

Insert Coin: 25
Amount Due: 25
Insert Coin: 25
Amount Due: 0
Change Owed: 0

```

### Example with Invalid Coins

```

Insert Coin: 25
Amount Due: 25
Insert Coin: 50
Amount Due: 25
Insert Coin: 1
Amount Due: 25
Insert Coin: 25
Amount Due: 0
Change Owed: 0

```

## Code Explanation

### Key Variables

- acceptable_coins: List of valid coin denominations as strings

- coin_sum: Running total of inserted coins

- coin_provided: User input for each coin

- change_owed: Amount to return if overpayment occurs

### Complete Source Code

```python

acceptable_coins = ['5', '10', '25']
coin_sum = 0

while coin_sum < 50:
coin_provided = input('Insert Coin: ')
if coin_provided in acceptable_coins:
coin_sum += int(coin_provided)
print('Amount Due:', 50 - coin_sum)

if coin_sum >= 50:
change_owed = coin_sum - 50
print('Change Owed:', change_owed)

```

## Features

- Input Validation: Only accepts specified coin denominations

- Running Total: Tracks total amount inserted

- Real-time Feedback: Shows remaining amount after each coin

- Change Calculation: Returns excess payment

- Simple Interface: Clear prompts and outputs

## Behavior Details

### Valid Coins

- 5 cents (nickel)

- 10 cents (dime)

- 25 cents (quarter)

### Invalid Input Handling

When invalid coins are inserted:

- The coin is rejected (not added to total)

- The amount due remains unchanged

- The program continues to accept coins

## Edge Cases

1. Exact Payment:

```

Coins: 25 + 25 = 50
Change Owed: 0

```

2. Overpayment:

```

Coins: 25 + 25 + 10 = 60
Change Owed: 10

```

3. Multiple Small Coins:

```

Coins: 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 = 50
Change Owed: 0

```

## Potential Improvements

### Enhanced Error Handling

```

acceptable_coins = ['5', '10', '25']
coin_sum = 0

while coin_sum < 50:
coin_provided = input('Insert Coin: ')
if coin_provided in acceptable_coins:
coin_sum += int(coin_provided)
else:
print(f"Invalid coin: {coin_provided}. Please insert 5, 10, or 25.")
print('Amount Due:', 50 - coin_sum)

if coin_sum >= 50:
change_owed = coin_sum - 50
print('Change Owed:', change_owed)

```

### Additional Features to Consider

1. Add a cancel transaction option

2. Implement a timeout feature

3. Track number of each coin type inserted

4. Add support for dollar bills

5. Include a receipt printing feature

## Alternative Implementation with Functions

```

def get_valid_coin():
acceptable_coins = ['5', '10', '25']
while True:
coin = input('Insert Coin: ')
if coin in acceptable_coins:
return int(coin)
print(f"Invalid coin. Please insert 5, 10, or 25.")

def vending_machine(target_amount=50):
coin_sum = 0

while coin_sum < target_amount:
coin_sum += get_valid_coin()
print('Amount Due:', target_amount - coin_sum)

change = coin_sum - target_amount
print('Change Owed:', change)
return change

if __name__ == "__main__":
vending_machine()

```

## Testing Scenarios

1. Test with exact payment combinations

2. Test with overpayment scenarios

3. Test with invalid inputs (letters, negative numbers, other denominations)

4. Test with empty input (just pressing Enter)

5. Test with very large overpayments

## Notes

- The script uses string comparison for coin validation

- No upper limit on overpayment amount

- The script runs until the target amount is reached or exceeded

- Invalid coins are silently ignored in the current implementation

## License

This script is provided as-is for educational and personal use.
