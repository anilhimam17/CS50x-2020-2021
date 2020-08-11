#include <stdio.h>

int main(void){

    char s[50];
    printf("Please enter your name and number: ");
    scanf("%s", s);

    FILE *ptr;
    ptr = fopen("read.txt", "a");
    fprintf(ptr, "%s", s);
    printf("The data was entered into the file\n");

    printf("THe data is being read from the file\n");
    ptr = fopen("read.txt", "r");
    fscanf(ptr, "%s", s);
    printf("The data read was: %s\n", s);

    fclose(ptr);
}