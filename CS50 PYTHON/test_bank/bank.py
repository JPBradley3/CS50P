## Get the users input as a greeting to compare later in the code
def main():

    greet = input("Please type in a US English greeting: ").lower().strip()
    print(f"${value(greet)}")
## Match the users input to acceptable inputs and return an output as defined in the problem set


def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
