from cs50 import get_float

# The main function of the program


def main():

    # Flag varibale for the correction of user inout
    run = True
    while run:

        # Takes the input for the change owed from the counter.
        change = get_float("Change Owed: ")

        if change < 0:
            pass

        else:
            run = False

    # Function to calculate the change owed.
    coins = change_owed(change)

    # Prints the end result
    print(coins)


# Function to calculate the change owed
def change_owed(change):

    coin_count = 0

    # Deducing the no of quaters required
    while change >= 0.25:
        change -= 0.25
        coin_count += 1

    change = round(change, 2)

    # Deducing the no of dimes required
    while change >= 0.10:
        change -= 0.10
        coin_count += 1

    change = round(change, 2)

    # Deducing the no of nickels required
    while change >= 0.05:
        change -= 0.05
        coin_count += 1

    change = round(change, 2)

    # Deducing the no of pennies required
    while change >= 0.01:
        change -= 0.01
        coin_count += 1

    return coin_count


if __name__ == "__main__":
    main()