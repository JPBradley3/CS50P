#### This is the basic starting point
#### From here we can take in one name

## name = input("Whats your name: ")

## print(f"hello, {name}!")


#### This is an expansion of our code that will show us how we can add multiple names.

## names = []

## for _ in range(3):
##    names.append(input("Whats your name: "))

## for name in sorted(names):
##    print(f"Hello, {name}!")


#### How do we call a file to edit instead:
#### In file.open there is "a" for append "w" for write

name = input("Whats your name: ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

