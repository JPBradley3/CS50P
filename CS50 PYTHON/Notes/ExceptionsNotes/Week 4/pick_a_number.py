import random

def main():
    maximum = int(input("Please enter the maximum number: "))
    print(rand_game(maximum))


def rand_game(maximum):
    while True:
        try:
            x = random.randint(0, maximum)
            return x
        except (SyntaxError, TypeError):
            break

main()




