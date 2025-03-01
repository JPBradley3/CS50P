camelCase = input("Please enter the camel case file name: ")
print("snake_case: ", end="")

for n in camelCase:
    if n.islower():
        print(n, end="")
    else:
        print("_" + n.lower(), end="")
print("")
