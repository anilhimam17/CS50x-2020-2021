from cs50 import get_string


def main():

    # Acquires the input string
    string = get_string("Text: ")

    # Stores the result - readability value
    result = readability(string)

    if result < 1:
        print("Before Grade 1")

    elif result >= 16:
        print("Grade 16+")

    else:
        print(f"Grade {result}")


def readability(string):

    # Respective counters
    sentence_count = 0
    word_count = 1
    letter_count = 0

    # Calculating the values for the counters in the given string
    for i in range(len(string)):
        if string[i].isalpha():
            letter_count += 1

        elif string[i].isspace():
            word_count += 1

        elif string[i] in [".", "?", "!"]:
            sentence_count += 1

    # Coleman-Liau Index (0.0588 * L) - (0.296 * S) - 15.8
    l_val = 0.0588 * ((letter_count / word_count) * 100)
    m_val = 0.296 * ((sentence_count / word_count) * 100)

    # Final value for readability of the text
    fin_val = round(l_val - m_val - 15.8)

    '''
    Check for all the values
    print(f"\n\nLetter(s): {letter_count}")
    print(f"Word(s): {word_count}")
    print(f"Sentence(s): {sentence_count}")
    '''

    return fin_val


# Standard test for executing the program from terminal
if __name__ == "__main__":
    main()