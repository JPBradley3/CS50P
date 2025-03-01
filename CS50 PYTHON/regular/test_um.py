import sys
from um import count

def main():
    pass

def test1():
    assert count("This is a test") == 0

def test2():
    assert count("This is um a test.") == 1

def test3():
    assert count("Um, This is a um, test...") == 2

main()
