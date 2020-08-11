#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //Here we take a user input for the string value of there name.
    string name = get_string("Please enter you name here:\n");

    //We then print the formatted string
    printf("Hello : %s\n", name);
}