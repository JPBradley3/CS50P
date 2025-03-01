#### The same principles can be applied to the read function to extract data from the file that we are working with.

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
