# Bitcoin Price Calculator

A Python Script for Real-Time Bitcoin Value Conversion

## Overview

This Python script fetches the current Bitcoin price from the CoinCap API and calculates the USD value for a specified amount of Bitcoin. It demonstrates API integration, command-line argument handling, and real-time cryptocurrency pricing.

## Requirements

- Python 3.x

- requests library

- Active internet connection

## Installation

Install the required requests library:

```

pip install requests

```

## Usage

### Command Syntax

```

python bitcoin.py <amount>

```

Where <amount> is the number of Bitcoins you want to convert to USD.

### Examples

```

$ python bitcoin.py 1
1
$45,234.5678

$ python bitcoin.py 0.5
0.5
$22,617.2839

$ python bitcoin.py 2.5
2.5
$113,086.4195

```

## Code Explanation

### Main Components

1. main() - Orchestrates the program flow

2. get_coin() - Validates and retrieves the command-line argument

3. req_coin() - Makes API request and calculates USD value

### API Details

- Endpoint: https://api.coincap.io/v2/assets/bitcoin

- Returns: JSON object with current Bitcoin price data

- No authentication required

- Updates in real-time

### Complete Source Code

```python

import sys
import requests
import json

def main():
g = get_coin()
req_coin(g)

def get_coin():
#print(sys.argv)
if len(sys.argv) == 2:
try:
if float(sys.argv[1]):
return sys.argv[1]
except ValueError:
print("Command-line argument is not a number")
sys.exit(1)
else:
print("Missing command-line argument")
sys.exit(1)

def req_coin(gcoin):
req = requests.get("https://api.coincap.io/v2/assets/bitcoin")
data = req.json()
usd = data["data"]["priceUsd"]
result = float(usd) * float(gcoin)
print(gcoin)
print(f"${result:,.4f}")

main()

```

## Features

- Real-Time Pricing: Fetches current Bitcoin price from CoinCap API

- Command-Line Interface: Easy to use from terminal

- Input Validation: Checks for proper numeric input

- Formatted Output: Displays USD value with commas and 4 decimal places

- Error Handling: Graceful handling of invalid inputs

## Error Handling

The script handles two main error cases:

1. Missing Argument:

```

$ python bitcoin.py
Missing command-line argument

```

2. Invalid Argument:

```

$ python bitcoin.py abc
Command-line argument is not a number

```

## API Response Format

The CoinCap API returns data in this structure:

```

{
"data": {
"id": "bitcoin",
"rank": "1",
"symbol": "BTC",
"name": "Bitcoin",
"priceUsd": "45234.5678",
...
}
}

```

## Potential Improvements

1. Add error handling for network failures

2. Support for multiple cryptocurrencies

3. Add caching to reduce API calls

4. Include historical price comparison

5. Add support for different output currencies

### Improved Error Handling Example

```

def req_coin(gcoin):
try:
req = requests.get("https://api.coincap.io/v2/assets/bitcoin", timeout=5)
req.raise_for_status()
data = req.json()
usd = data["data"]["priceUsd"]
result = float(usd) * float(gcoin)
print(gcoin)
print(f"${result:,.4f}")
except requests.RequestException as e:
print(f"Error fetching Bitcoin price: {e}")
sys.exit(1)
except KeyError:
print("Invalid API response format")
sys.exit(1)

```

## Testing Suggestions

- Test with various numeric inputs (integers, floats, negative numbers)

- Test with invalid inputs (strings, special characters)

- Test with no arguments or multiple arguments

- Test network failure scenarios

## Notes

- The CoinCap API is free but may have rate limits

- Bitcoin prices are highly volatile

- The script requires an active internet connection

- Prices are in USD by default
