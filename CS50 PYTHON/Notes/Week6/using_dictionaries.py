students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")


## Create a dictionary

        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

## The dictionary kicks its data to the list of students at the top of the code.

for student in students:
    ## Single quotes are used below because when you are staying in python to grab variables their containers follow rules of containerization
    ## In this instance we have the dictionary python variables above that are then printed variables that python will need to know are different
    ## They are different in that they are no longer manipulable in any other python way than printing
    print(f"{student['name']} is in {student['house']}")
