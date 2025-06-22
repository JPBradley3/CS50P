# Cookie Jar Class and Tests

## Overview

This package consists of a Python class, `Jar`, which models a cookie jar with user-defined capacity and supports deposit and withdrawal of cookies. The jar representation can be printed as a string of cookies (🍪), and the class includes error-checking for overfilling and over-emptying.
Also included are unit tests for the class using `pytest`.

## Features

- Set and get the jar's capacity.

- Track the current number of cookies in the jar.

- Add (deposit) or remove (withdraw) cookies with automatic error handling.

- Pretty string representation using emoji.

- Tested with `pytest`.

## Requirements

- Python 3.x

- `pytest` package for running tests (`pip install pytest`)

## Usage

### Class Usage Example

```

from jar import Jar

jar = Jar(10)      # Create a jar with capacity 10
jar.deposit(5)     # Add 5 cookies
jar.withdraw(2)    # Remove 2 cookies
print(str(jar))    # Output: 🍪🍪🍪
print(jar.size)    # Output: 3
print(jar.capacity)# Output: 10

```

### Command Line

1. Save your class in a file `jar.py`.

2. To run the main demonstration function (which adds and removes cookies):

```

python jar.py

```

3. To run tests:

```

pytest jar_test.py

```

where `jar_test.py` contains your test functions.

## Class API

- `Jar(capacity=12)`: Create a cookie jar with optional integer `capacity` (default 12).

- `deposit(n)`: Add `n` cookies. Raises `ValueError` if exceeding capacity.

- `withdraw(n)`: Remove `n` cookies. Raises `ValueError` if taking more than present.

- `capacity`: Property for getting/setting capacity. Cannot be negative.

- `size`: Property for getting/setting current cookie count. Must be in valid range.

- `str(jar)`: Returns a string of cookies proportional to the current size.

## Testing

```

def test__init():
jar = Jar(2)
assert jar.capacity == 2

def test_str():
jar = Jar(4)
jar.deposit(2)
assert str(jar) == "🍪🍪"

def test_deposit():
jar = Jar(12)
jar.deposit(8)
assert jar.size == 8
with pytest.raises(ValueError):
jar.deposit(14)

def test_withdraw():
jar = Jar(12)
jar.deposit(12)
jar.withdraw(5)
assert jar.size == 7
with pytest.raises(ValueError):
jar.withdraw(10)

```

## Notes and Caveats

- The `deposit` method checks that the jar does not exceed its capacity.

- The `withdraw` method checks that you do not remove more cookies than present.

- Unicode emoji may display differently depending on your system.

- Class uses Python’s `property` decorator for robust attribute management.
