## sys.argv = system argument vector and the variable is a list that means that the first element is the first thing that typed and as you go it adds elements

## We can assume that sys.argv is always the user input at the command line if they put any in and we will need to do error exceptions to allow for no input and prompt the user for some

import sys

try:
    print("hello, my name is ", sys.argv[1])
except IndexError:
    print(f"Please put a space and your name after 'notes.py' in the Terminal.")


