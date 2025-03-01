## Narrow down functions to the needed function and keep the program pythonic instead of programmatic.

from emoji import emojize

x = input("EInput: ")

## Included language="alias" in order to format for words around the emoji.
print("Output:", emojize(x, language="alias"))
