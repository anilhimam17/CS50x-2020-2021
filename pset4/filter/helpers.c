#include "helpers.h"
#include <stdio.h>
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //Takes all the current pixels
            int curr_red = image[i][j].rgbtRed;
            int curr_blue = image[i][j].rgbtBlue;
            int curr_green = image[i][j].rgbtGreen;

            //Checks for equality
            if (curr_red == curr_blue && curr_red == curr_green)
            {
                image[i][j].rgbtRed = curr_red;
                image[i][j].rgbtBlue = curr_red;
                image[i][j].rgbtGreen = curr_red;
            }

            //Using the average method
            else
            {
                int avg_pix = round((float)(curr_red + curr_blue + curr_green) / 3);

                image[i][j].rgbtRed = avg_pix;
                image[i][j].rgbtBlue = avg_pix;
                image[i][j].rgbtGreen = avg_pix;
            }
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //Calculating the sepia values
            int sepiaRed = round((float)((.393 * image[i][j].rgbtRed) + (.769 * image[i][j].rgbtGreen) + (.189 * image[i][j].rgbtBlue)));
            int sepiaGreen = round((float)((.349 * image[i][j].rgbtRed) + (.686 * image[i][j].rgbtGreen) + (.168 * image[i][j].rgbtBlue)));
            int sepiaBlue = round((float)((.272 * image[i][j].rgbtRed) + (.534 * image[i][j].rgbtGreen) + (.131 * image[i][j].rgbtBlue)));

            //Setting the values within limits
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }

            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;

        }
    }
    return;
}

void reflect_reflect(RGBTRIPLE *left_pix, RGBTRIPLE *right_pix)
{

    RGBTRIPLE temp = *left_pix;
    *left_pix = *right_pix;
    *right_pix = temp;

}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {

            //Swapping the values for reflection
            reflect_reflect(&image[i][j], &image[i][width - j - 1]);
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE curr_pix = image[height][width];
            int sum_val_red = 0;
            int sum_val_green = 0;
            int sum_val_blue = 0;

            int avg_val_red = 0;
            int avg_val_green = 0;
            int avg_val_blue = 0;

            if (i - 1 >= 0 && i + 1 < height)
            {

                if (j - 1 >= 0 && j + 1 < width)
                {

                    //----------------------------
                    sum_val_red = (image[i - 1][j - 1].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed + image[i][j - 1].rgbtRed + image[i][j].rgbtRed + image[i][j + 1].rgbtRed + image[i + 1][j - 1].rgbtRed + image[i + 1][j].rgbtRed + image[i + 1][j + 1].rgbtRed);
                    avg_val_red = round((float) sum_val_red / 9);

                    //----------------------------
                    sum_val_green = (image[i - 1][j - 1].rgbtGreen + image[i - 1][j].rgbtGreen + image[i - 1][j + 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i][j].rgbtGreen + image[i][j + 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen + image[i + 1][j].rgbtGreen + image[i + 1][j + 1].rgbtGreen);
                    avg_val_green = round((float) sum_val_green / 9);

                    //----------------------------
                    sum_val_blue = (image[i - 1][j - 1].rgbtBlue + image[i - 1][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i][j].rgbtBlue + image[i][j + 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue + image[i + 1][j].rgbtBlue + image[i + 1][j + 1].rgbtBlue);
                    avg_val_blue = round((float) sum_val_blue / 9);

                    //----------------------------
                    image[i][j].rgbtRed = avg_val_red;
                    image[i][j].rgbtGreen = avg_val_green;
                    image[i][j].rgbtBlue = avg_val_blue;
                }
            }

        }
    }
}
