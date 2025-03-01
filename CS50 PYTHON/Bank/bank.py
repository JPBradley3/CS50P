## Get the users input as a greeting to compare later in the code
def main():


greeting = input("Please type in a US English greeting: ")


## Convert the greeting to be fair to capitalization

lowercase_greeting = greeting.lower()
stripped_answer = lowercase_greeting.strip()

## Match the users input to acceptable inputs and return an output as defined in the problem set

if stripped_answer.startswith(("hello")):
    print("$0")
elif stripped_answer.startswith(("h")):
    print("$20")
else:
    print("$100")


