## There is a framework that youcan use called "pytest" to replace the huge amount of code that the last notes took
## You are able to run PyTest from the terminal window.
## In addition to that you can call PyTest from the code itself as class points out with strings.

import pytest
from Notes.TestsNotes.TestIntegers.calculator import square

def main():
    test_positive()
    test_negative()
    test_zero()

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


if __name__ == "__main__":
    main()
