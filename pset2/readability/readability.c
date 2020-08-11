#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>


int main(void)
{
    //Acquring user input for the string to be graded
    string sentence = get_string("Text :");

    int length = strlen(sentence);
    int letters = 0;
    int words = 1;
    int lines = 0;

    for (int i = 0; i < length; i++)
    {
        //Counting all the letters
        if (isalpha(sentence[i]))
        {
            letters += 1;
        }

        //Counting all the words
        if (isspace(sentence[i]))
        {
            words += 1;
        }

        //Counting the sentences
        if ((sentence[i] == '.') || (sentence[i] == '!') || (sentence[i] == '?'))
        {
            lines += 1;
        }

    }

    //Checking the value of the variables while testing
    printf("%d letter(s)\n", letters);
    printf("%d word(s)\n", words);
    printf("%d sentence(s)\n", lines);

    //Solving the equation part by part
    float val1 = 0.0588 * ((letters / (float)words) * 100);
    float val2 = 0.296 * ((lines / (float)words) * 100);
    int index = round(val1 - val2 - 15.8);

    //Checking for the different grade values
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

    //Exit status of the program
    return 0;

//22.4
}