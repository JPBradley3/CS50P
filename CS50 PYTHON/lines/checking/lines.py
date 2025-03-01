import sys

# Main function
def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".py"):
            sys.exit("Not a python file")
        else:
            print(read_data(sys.argv[1]))

# Function to read and count relevant lines from a file
def read_data(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Count lines that are not comments or whitespace
        # Count is set to zero to use a simple addition function below
        count = 0
        for line in lines:

            # Here is where "strip" is used to remove white space from "str"
            stripped = line.strip()

            ## Here is where we search the file for comments and remove them from the count after setting the variable
            ## Count to zero
            if stripped and not stripped.startswith("#"):
                count += 1
        return count
    except FileNotFoundError:
        sys.exit("File does not exist")


# Call the main function
if __name__ == "__main__":
    main()
