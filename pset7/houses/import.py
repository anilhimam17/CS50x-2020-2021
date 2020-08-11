from sys import argv
from cs50 import SQL

# Initialising the database to enter the data
db = SQL("sqlite:///students.db")


def main():
    # The main function of the program
    # Opening the file with file handling
    with open(argv[1], 'r') as myfile:
        lines = myfile.readlines()

        # Removing the header of the file
        lines = lines[1:]

    # ID VALUE
    count = 0

    # Inserting the data into the database
    for row in lines:

        # Incrementing the id value
        count += 1

        # Dividing the row into its components for entering the data
        sub = row.split(',')

        # Working on the name
        name = sub[0].split()

        if len(name) == 2:
            first_name, middle_name, last_name = name[0], None, name[1]

        else:
            first_name, middle_name, last_name = name[0], name[1], name[2]

        # Assigning the house
        house = sub[1]

        # Assigning the birthyear
        year = int(sub[2].strip())

        # Finally inserting all the values into the database
        if len(name) == 2:
            db.execute("insert into students values (?, ?, ?, ?, ?, ?)", count, first_name, middle_name, last_name, house, year)

        else:
            db.execute("insert into students values (?, ?, ?, ?, ?, ?)", count, first_name, middle_name, last_name, house, year)


if len(argv) != 2:
    print("Usage: import.py <name of csv file>")
    quit()

main()


'''
Table schema JUST INCASE I DELETED IT.
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first VARCHAR(255),
    middle VARCHAR(255),
    last VARCHAR(255),
    house VARCHAR(10),
    birth INTEGER
);'''