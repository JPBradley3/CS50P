## Cleaning the user input

#name = input("What's your name? ").strip()
#print(f"hello, {name}")

## What if the user used LAST, FIRST
## we would need to edit this to be able to adapt to a different kind of input.

#name = input("What's your name? ").strip()
#if "," in name:
#    last, first = name.split(", ")
#    name = f"{first} {last}"
#print(f"hello, {name}")

## This would get the job done but doesnt also allow for expansion in our code to be able to take input and parse it for what we want.


import re

name = input("What's your name? ").strip()

## we search the string for a pattern that is read by python as a variable MATCHES
#### Remember that parenthesis are for

######## (...)   a group
############ This will pass a TRUE or a FALSE depending on if you are being explicit inside the parenthetical

######## (?:...) non-caputuring version
############ This will ignore the group to pass it through to a TRUE value

matches = re.search(r"^(.+), (.+)$", name)


## Search for matches with a BOOLEAN argument:

if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"Hello, {name}")
