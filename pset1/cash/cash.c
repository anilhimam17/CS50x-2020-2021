#include <stdio.h>
#include <cs50.h>
#include <math.h>

//Function Prototype
int counter(float change);

//Main Function
int main(void)
{
    printf("Welcome to Problem Set 1\n");

    bool run = true;
    float money;

    while (run)
    {
        money = get_float("Enter the change to be owed:");

        if (money <= 0)
        {
            printf("-----Please enter a positive value for the change (Greater than 0)-----\n");

        }

        else
        {
            run = false;

        }

    }

    int result = counter(money);
    printf("%i\n", result);

    return 0;

}

//Calculating function
int counter(float change)
{
    //Type casting to an integer to deal with rounding values easily
    change = (int)round(change * 100);

    //------------------------------------------------

    int count_25 = 0;
    while (change >= 25)
    {
        change -= 25;
        count_25 += 1;

    }

    //------------------------------------------------

    int count_10 = 0;
    while (change >= 10)
    {
        change -= 10;
        count_10 += 1;

    }

    //------------------------------------------------

    int count_5 = 0;
    while (change >= 5)
    {
        change -= 5;
        count_5 += 1;

    }

    //------------------------------------------------

    int count_1 = 0;
    while (change >= 1)
    {
        change -= 1;
        count_1 += 1;

    }
    return (count_25 + count_10 + count_5 + count_1);

}
