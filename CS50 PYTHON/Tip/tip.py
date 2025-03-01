## Started with the main function which has dollars and percentages collected as strings.

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    ## Percent is still a float that has to be converted into a percent and that can be edited here to take care of the problem)
    tip = dollars * (percent/100)

    ## Printing as given in the problem set using pythons internal formatting to limit things to 2 decimal places and rounding up.
    print(f"Leave ${tip:.2f}")



## This formatting takes the answer to the input and converts it to be read as a float.



## It wraps it up in the variable "d" and then sends it back up to sit inside "Line 4"
def dollars_to_float(d):
    d = float(d)
    return(d)

 ## It wraps it up in the variable "p" and then sends it back up to sit inside "Line 5"
def percent_to_float(p):
    p = float(p)
    return(p)


main()
