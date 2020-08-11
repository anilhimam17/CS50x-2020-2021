#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>

//Function Prototypes
int checking_int(string input);
void caesar_encryption(int shift_key_1);
int convert(int shift_key_2, int ord_value);

//Main Function
int main(int argc, string argv[])
{
    //If arguments provided match the requirement
    if (argc == 2)
    {
        int result_1 = checking_int(argv[1]);

        //To confirm the key given was an integer
        if (result_1 == 1)
        {
            printf("The input recieved was a valid integer, proceeding with the program\n");

            //Conversion of string to int
            int key = atoi(argv[1]);

            //Proceeding to the encryption
            caesar_encryption(key);
            return 0;
        }

        //Incase the given key value wasnt an integer
        else
        {
            printf("The given input wasnt a valid number\n");
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    //Incase the given key value is not what was expected
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

}

//Function responsible for giving an emperical result of the encryption formula
int convert(int shift_key_2, int ord_value)
{
    //Emperical value of the encryption algo
    return ord_value + shift_key_2 % 26;
}

//Function responsible for the logic of the problem statement
void caesar_encryption(int shift_key_1)
{

    //Getting the plaintext to be converted to cipher text
    string plain_text = get_string("plaintext: ");

    //Getting the length
    int length = strlen(plain_text);

    //Shifted array
    int shift_array[length];

    //Encipher the text
    for (int i = 0; i < length; i++)
    {
        //Present value of the plaintext in the loop
        char val_now = plain_text[i];

        //Ordinal value of the present value in the loop
        int ord_val = (int) val_now;

        //Emperical result of the algo wrt to the value
        int result = convert(shift_key_1, ord_val);

        //If the value is alphabet
        if (isalpha(val_now))
        {

            //If the value is a capital case alphabet
            if (ord_val >= 97 && ord_val <= 122)
            {

                //Warp - up for out of bounds errors
                if (result > 122)
                {
                    int val_mod_1 = result;
                    val_mod_1 -= 122;
                    val_mod_1 += 96;
                    shift_array[i] = val_mod_1;
                }

                //Incase not out of bounds
                else
                {
                    shift_array[i] = result;
                }
            }

            //If the value is a smaller case alphabet
            else
            {

                //Warp - up for out of bounds errors
                if (result > 90)
                {
                    int val_mod_2 = result;
                    val_mod_2 -= 90;
                    val_mod_2 += 64;
                    shift_array[i] = val_mod_2;
                }

                //Incase not out of bounds
                else
                {
                    shift_array[i] = result;
                }
            }

        }

        //Incaes the value present in the loop is not an alphabet
        else
        {
            shift_array[i] = ord_val;
        }

    }

    //Printing the array of ciphertext
    printf("ciphertext: ");
    for (int i = 0; i < length; i++)
    {
        //Converting the ordinal values to charecters of ciphertext
        printf("%c", shift_array[i]);
    }
    //Line termination
    printf("\n");
}


//Function to to check whether input is a number or not
int checking_int(string input)
{

    //Length of given terminal input
    int length = strlen(input);

    //Parity check
    int digit_count = 0;

    for (int i = 0; i < length; i++)
    {
        //Checking whether digit or not
        if (isdigit(input[i]))
        {
            digit_count += 1;
        }
    }

    //Check sum for the no of values provided in input
    if (digit_count == length)
    {
        //Is and integer
        return 1;
    }

    else
    {
        //Is not an integer
        return 0;
    }
}

