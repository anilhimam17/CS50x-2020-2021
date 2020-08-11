#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>

//Custom datatype
typedef struct{
    string name;
    int votes;
}candidate;

int main (int agrc, string argv[]){

    candidate candidates[atoi(argv[1])];

    for (int i = 0; i < atoi(argv[1]); i++){
        candidates[i].name = get_string("Enter the name of the candidate:");
        candidates[i].votes = get_int("Enter the no of initial votes acquired:");
    }

    for (int i = 0; i < atoi(argv[1]); i++){
        printf("The name of the given candidate was: %s\n", candidates[i].name);
        printf("The no of votes was: %i\n", candidates[i].votes);
        printf("The index of the candidate was: %i\n", i);
    }
    return 0;
}