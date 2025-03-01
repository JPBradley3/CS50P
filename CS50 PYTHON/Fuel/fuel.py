## Define the main and get faction functions to pass a float back to main to print a percent.


## Main function passes the input from "get_fraction" to a calculation of the percentage that uses styling to round to the next highest number.
def main():
    fuel = float(get_fraction("What is your fraction:"))
    print(f'{round(fuel * 100)}%')

## "get_fraction" function takes the input and splits the variables up to divide the input as a float for accuracy back
## to main and then returns the fuel percentage.
def get_fraction(prompt):
    while True:
        try:
            x = (input(prompt).split('/'))
            if round(int(x[0]) / int(x[1]), 1) == 1:
                print("F")
                exit()
            elif (int(x[0]) == 0) or (int(x[1]) == 100):
                print("E")
                exit()
            elif (int(x[0]) < int(x[1])):
                return float(x[0]) / float(x[1])
        except (ValueError, ZeroDivisionError):
            pass


## Calls the main function to begin the calculation and print the rest f the program.
main()

