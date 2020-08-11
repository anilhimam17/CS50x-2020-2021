#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    int array[2][5] = {{1,2,3,4,5}, {6,7,8,9,0}};

    int count_h = 2;
    int count_w = 5;

    int it_val = 1;
    int wi_val = 1;

    if (it_val < count_h && wi_val - 1 >= count_w){
        int avgr = (array[it_val][wi_val - 1] + array[it_val][wi_val] + array[it_val][wi_val + 1] +
        array[it_val + 1][wi_val - 1] + array[it_val + 1][wi_val] + array[it_val + 1][wi_val + 1]);
    }

    printf("The new pix val is: %i\n", avgr);
}

