## We can become more sophisticated in our code and use built in dictionaries to search for more expected kinds of things
## Like when email servers get slammed by aaaaa@email.com due to DDoS attacks or when Target got hacked through SQL email manipulations
## Things like pattern recognition and enforcing more secure kinds of nomenclatures with the user base adds to security and cleans up the way forward to adapt to their needs.

import re

email = input("What's your email? ").strip().lower()

if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")


#### These are the operators that make chunks of data more easier to enforce scan and manipulate:

    #### \d    decimal digit
    #### \D    not a decimal digit
    #### \s    whitespace characters
    #### \S    not a whitespace character
    #### \w    word character, as well as numbers and the underscore which matches the IDE and compilers needs
    #### \W    not a word character

    #### A|B     either A or B
    #### (...)   a group
    #### (?:...) non-capturing version

    #### Like in if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email): for different email extensions.
    
