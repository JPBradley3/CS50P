# IPv4 Address Validator

*Your Name*

*July 15, 2025*

## Introduction

This project provides a Python utility for validating IPv4 addresses. It consists of a main module (numb3rs.py) that contains the validation logic and a test module that verifies the implementation.

## Features

- Validates standard IPv4 addresses (e.g., 192.168.1.1)

- Handles special cases like localhost (127.0.0.1) and broadcast addresses (255.255.255.255)

- Rejects invalid formats and values outside the valid range (0-255 for each octet)

- Includes comprehensive test suite

## Installation

No special installation is required. Simply download the files to your local directory:

```

git clone https://github.com/yourusername/ipv4-validator.git
cd ipv4-validator

```

## Usage

### As a Module

You can import the validation function into your own code:

```

from numb3rs import validate

# Check if an IP address is valid
if validate("192.168.1.1"):
print("Valid IP address")
else:
print("Invalid IP address")

```

### Running Tests

To run the test suite:

```

pytest test_numb3rs.py

```

or using Python directly:

```

python test_numb3rs.py

```

## Implementation Details

### numb3rs.py

The main module contains the validate function which:

- Takes a string as input

- Returns True if the string represents a valid IPv4 address

- Returns False otherwise

```python

def validate(ip):
"""
Validates if the input string is a valid IPv4 address.
Each octet must be between 0 and 255, inclusive.

Args:
ip (str): The string to validate

Returns:
bool: True if valid IPv4 address, False otherwise
"""

# Implementation details...

```

### test_numb3rs.py

The test module contains a comprehensive set of test cases:

```python

def test_validate():
assert validate("127.0.0.1") == True      # localhost
assert validate("255.255.255.255") == True # broadcast
assert validate("512.512.512.512") == False # values > 255
assert validate("1.2.3.1000") == False    # last octet > 255
assert validate("cat") == False           # non-numeric
assert validate("1.2.3.4") == True        # standard valid IP
assert validate("11.99.22.88") == True    # standard valid IP
assert validate("199.911.288.882") == False # multiple invalid octets
assert validate("249.249.249.249") == True  # valid high numbers

```

## Test Cases

The test suite verifies that the validate function correctly:

- Accepts valid IPv4 addresses in standard format

- Rejects values where any octet exceeds 255

- Rejects non-numeric input

- Handles edge cases like broadcast addresses

## Requirements

- Python 3.6 or higher

- pytest (optional, for running tests)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
