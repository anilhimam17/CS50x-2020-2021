#include <stdio.h>
#include <cs50.h>

int main(void){

    int preferences[5][2] = {{0, 1}, {1, 2}, {2, 0}, {0, 1}, {1, 2}};
    int count_1 = 0;
    int count_2 = 0;
    int count_0 = 0;

    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++){
            if (preferences[i][j] == j){
                printf("The value of preferences was: %i\n", j);
            }
        }
    }
}