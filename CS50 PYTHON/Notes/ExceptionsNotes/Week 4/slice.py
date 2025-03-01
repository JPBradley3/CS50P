import sys

if len(sys.argv) < 2:
    sys.exit("Too many arguments")

## This is a slice (where you can see the square bracket the number represents the element that it is starting with.)
for arg in sys.argv[1:]:
    print("hello, my name is", arg)

