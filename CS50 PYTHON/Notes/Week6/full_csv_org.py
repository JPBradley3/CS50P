#### We can also rely on other formats of CSV that have their columns and rows labeled.
#### This changes the top line of the txt version to reflect the variables as their identifiers separated by commas.

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    ### This line creates a dictionary as a function of memory when Python reads the CSV file without all of the additional formatting.
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    ### Now our rows are easier to write for in a more pythonic linearity.
    writer.writerow({"name": name, "home": home})


## Python will escape addresses with additional commas since it will get read by the compiler as different arguments following NAME or ADDRESS
