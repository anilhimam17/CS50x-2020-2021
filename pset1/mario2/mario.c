#include <stdio.h>
#include <cs50.h>

//Function prototype
void towers(int heights);


//Main function
int main(void)
{

    printf("Welcome to Problem Set 1\n");

    bool run = true;
    int height;

    while (run)
    {

        //Takes the height input for the height of the tower.
        height = get_int("Please enter a number here for the height of the towers (1 - 8):");

        if ((height <= 0) || (height > 8))
        {
            printf("Enter a value within the range of 1 - 8\n");
        }

        else
        {
            run = false;
        }
    }

    //Function used for printing the towers.
    towers(height);

    return 0;
}


//Towers fn to print the mario towers
void towers(int heights)
{

    //Program logic
    for (int i = 1; i < (heights + 1); i++)
    {

        //Calc the no of spaces required
        int space_val = heights - i;

        //Prints the no of spaces calc --> Left side
        for (int j = 1; j <= space_val; j++)
        {
            printf(" ");

        }

        //Prints the no of #'s calc ---> Left side
        for (int k = 1; k <= i; k++)
        {
            printf("#");

        }

        //Gives the space in btw the towers
        printf("  ");

        //Prints the no of #'s calc ---> Right side
        for (int k = 1; k <= i; k++)
        {
            printf("#");

        }

        //Terminates the line
        printf("\n");

    }

}