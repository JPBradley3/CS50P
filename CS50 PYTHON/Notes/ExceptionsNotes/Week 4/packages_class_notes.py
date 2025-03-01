## This is an example of the resource in python called packages.
## CowSay and many others are available to use insteead of writing your own code.

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])


