#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#define BLOCKSIZE 512

int main(int argc, char *argv[])
{
    //If file name was not mentioned
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    //------------------------------------------------------

    //Reading the file of given name
    FILE *myfile = fopen(argv[1], "r");

    if (myfile == NULL)
    {
        //If file was not found
        printf("Error reading the file");
        return 1;
    }

    //------------------------------------------------------

    //New type to store byte date read from the raw file
    typedef uint8_t BYTE;
    BYTE buffer[BLOCKSIZE];

    //Jpeg counter
    int image_count = 0;

    //File pointer for the recoverd jpegs
    FILE *new_image = 0;

    //Filename for the new jpegs
    char filename[8];

    //While loop for processing the entire file
    bool run = true;
    while (run)
    {
        //Reading a block of data from the file
        size_t read_data = fread(buffer, sizeof(BYTE), BLOCKSIZE, myfile);

        if (read_data == 0 && feof(myfile))
        {
            run = false;
        }

        bool jpeg_check = buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0);

        if (jpeg_check && new_image != NULL)
        {
            image_count++;

            //Closing a previous jpeg to create a new jpeg
            fclose(new_image);

        }

        if (jpeg_check)
        {
            //Creating the modified name with the image counter
            sprintf(filename, "%03i.jpg", image_count);

            //Opening the new image
            new_image = fopen(filename, "w");

        }

        if (new_image != NULL)
        {
            //Writing the new information
            fwrite(buffer, sizeof(BYTE), BLOCKSIZE, new_image);
        }

    }

    //Clsoing the raw file
    fclose(myfile);

    //Closing the last created image
    fclose(new_image);

    return 0;
}
