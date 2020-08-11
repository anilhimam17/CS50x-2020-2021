#include <stdio.h>
#include <string.h>
#include <cs50.h>

int main(void){

    string name = get_string("Enter name: ");
    int length = strlen(name);

    for(int i = 0; i < length; i++){

        char arr_val = name[i];
        printf("%c", arr_val);
    }
    printf("\n");
}