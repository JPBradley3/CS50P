#### There is a library in python to manipulate the files as well.

import csv


#### Reformatting earlier code to utilize the csv library and make our life easier.

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
