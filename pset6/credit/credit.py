from cs50 import get_string

# The main function that runs the program


def main():

    # Takes the input for the credit card number
    card_number = get_string("Number: ")

    # Deploys Luhn's Algorithm on the given card number
    result = luhns_algo(card_number)

    # Checks for the result
    if result:
        # Evaluation for valid card
        if card_number[0:2] in ["34", "37"]:
            print("AMEX")

        elif card_number[0:2] in ["51", "52", "53", "54", "55"]:
            print("MASTERCARD")

        elif card_number[0] == "4":
            print("VISA")

    else:
        print("INVALID")


# Function for Luhn's algorithm
def luhns_algo(card_number):

    # Length of the card number
    length = len(card_number) - 1

    # List to store all even indexes second to last
    even = []

    # List to store all odd indexes second to last
    odd = []

    # Back indexing second to last
    for i in range(length - 1, -1, -2):
        even.append(int(card_number[i]))

    # Back indexing for the odd positions
    for i in range(length, -1, -2):
        odd.append(int(card_number[i]))

    # Multiplying all the elements by 2 and taking the sum
    sum_val = 0
    for i in range(len(even)):
        val = str(even[i] * 2)
        for i in val:
            sum_val += int(i)

    # Sum_val for all the digits not multiplied by 2
    for i in odd:
        sum_val += i

    if str(sum_val)[-1] == "0":
        return True

    else:
        return False


# The main function to run the program
if __name__ == "__main__":
    main()