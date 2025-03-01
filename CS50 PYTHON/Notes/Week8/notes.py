def main():

    name = get_name()

    house = get_house()

    print(f"{name}, {house}")


def get_name():
    name = input("Name: ")
    return name

########## Or return input("Name: ")



def get_house():
    house = input("House: ")
    return house

########## Or return input("House: ")


if __name__ == "__main__":
    main()
