#include <stdio.h>
#include <cs50.h>

//Function Prototype
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

    //Printing the towers using the function
    towers(height);

    return 0;
}


//Towers function
void towers(int heights)
{

    //Program logic
    for (int i = 1; i < (heights + 1); i++)
    {

        //No of empty spaces required
        int space_val = heights - i;
        int j = 1;

        //Printing the empty spaces
        while (j <= space_val)
        {
            printf(" ");
            j += 1;

        }

        //Printing the number of #'s
        for (int k = 1; k <= i; k++)
        {
            printf("#");

        }

        //Terminating the line
        printf("\n");
    }
}