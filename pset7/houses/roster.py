# Your program should accept the name of a house as a command-line argument.
# Your program should query the students table in the students.db database for all of the students in the specified house.
# Your program should then print out each student’s full name and birth year (formatted as, e.g., Harry James Potter, born 1980 or Luna Lovegood, born 1981).
# Students should be ordered by last name. For students with the same last name, they should be ordered by first name.
from sys import argv
from cs50 import SQL

# Initialising the database
db = SQL("sqlite:///students.db")


def main():
    # The main function of the program
    # Querying the table for the particular house
    result = db.execute("select * from students where house = ? order by last", argv[1])

    # Final sorting of all the elements
    for i in range(len(result)):
        if i + 1 < len(result) and result[i]["last"] == result[i + 1]["last"] and not (result[i]["first"] < result[i + 1]["first"]):
            temp = result[i]
            result[i] = result[i + 1]
            result[i + 1] = temp

    # Printing all the data
    for row in result:

        # Printing the name
        if row["middle"] == None:
            print(row["first"], row["last"], ", born", row["birth"])

        else:
            print(row["first"], row["middle"], row["last"], ", born", row["birth"])


if len(argv) != 2:
    print("Usage: import.py <name of house to be queried>")
    quit()

main()