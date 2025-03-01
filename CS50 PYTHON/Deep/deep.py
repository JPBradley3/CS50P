## Take user input to be able to convert the data for filtering andd create a variable.

answer = input("What is the answer to the great question what is life, the universe, and everything?: ")

## Convert the data and make it readable for the function of the program [COMPARISON]

## Convert to lower case
lowercase_answer = answer.lower()

## Convert to minimum characters omitting spaces
stripped_answer = lowercase_answer.strip()

## Take the stripped and formatted answer and run it through the conditionals to find a match
## in our comparison
if stripped_answer == "forty-two":
    print("Yes")
elif stripped_answer == "forty two":
    print("Yes")
elif stripped_answer == "42":
    print("Yes")
else:
    print("No")

