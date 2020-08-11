from sys import argv
import os
import csv


def main():

    # To split the path for accessing the csv file
    directory, csv_name = argv[1].split("/")

    # To change directory to access the required csv
    os.chdir(directory)

    # Opens the csv file
    dls = []
    with open(csv_name, newline="") as csv_file:
        data = csv.reader(csv_file)
        for i in data:
            dls.append(i)

    # removing the first row of data
    dls = dls[1:]

    # ---------------------------------------------------

    # Getting back to the main DNA Directory
    os.chdir("..")

    # To split the path for accessing the raw dna sequence
    directory, seq = argv[2].split("/")

    # To change directory to access the required dna
    os.chdir(directory)

    # Read the dna sequence
    with open(seq, "r") as dnafile:
        dna_seq = dnafile.read()

    # ---------------------------------------------------
    # The main algorithm to analyse all the dna strs

    length = len(dna_seq)
    strs = {"AGATC": [], "TTTTTTCT": [], "AATG": [], "TCTAG": [], "GATA": [], "TATC": [], "GAAA": [], "TCTG": []}
    i = 0
    rep = ""
    count = 0

    while i < length:

        if dna_seq[i: i + len(rep)] != rep and rep != "":
            strs[rep].append(count)
            count = 0

        if dna_seq[i: i+4] in ["AATG", "GATA", "TATC", "GAAA", "TCTG"]:
            count += 1
            rep = dna_seq[i: i+4]
            i += 4

        elif dna_seq[i: i+5] in ["AGATC", "TCTAG"]:
            count += 1
            rep = dna_seq[i: i+5]
            i += 5

        elif dna_seq[i: i+8] == "TTTTTTCT":
            count += 1
            rep = "TTTTTTCT"
            i += 8

        else:
            i += 1

    # Final result of all the traits computed from the strs
    traits = [0]
    for i in strs.values():
        if i != []:
            traits.append(max(i))

    # Comparing with the database to find the results
    for i in dls:
        sim = 0
        for j in range(1, len(i)):
            if int(i[j]) == traits[j]:
                sim += 1
            if sim >= 6 and len(i) == 9:
                print(i[0])
                quit()

            if sim >= 2 and len(i) == 4:
                print(i[0])
                quit()

    else:
        print("No match")


# To check for a minimum of 3 arguments as a must.
if len(argv) != 3:
    print("Usage: <Program Name> <CSV Name> <RAW DNA FILE NAME>")

# To run the program
else:
    main()