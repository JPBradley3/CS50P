## Set up main function and get total started at zero to be able to do math in the exception loop.

def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    total = 0

    ## In the exception loop we can add items and format them to index to the dictionary. The final line allows "CTRL+D" to function as an escape.
    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                total += menu[item]
                print(f'Total: ${total:.2f}')
            else:
                break
        except EOFError:
            print()
            break

main()

