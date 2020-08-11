from cs50 import get_int

# The main function


def main():

    run = True
    while run:
        # Taking the input for the height of the towers
        height = get_int("Height: ")

        # Checking for the bounds of the value given
        if height <= 8 and height > 0:
            run = False
        else:
            pass

    # Printing the towers for the given height on the left hand side
    for i in range(1, height + 1):

        # Calculating and printing the no of space required
        print(" " * (height - i), end="")

        # Calculating and printing the no of hashes required
        print("#" * i, end="")

        # Printing the space in between the towers
        print("  ", end="")

        # Calculating and printing the no of hashes required
        print("#" * i)


# Standard execution of the main function
if __name__ == "__main__":
    main()
