#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>


int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: convert inputfile\n");
        return 1;
    }

    // remember filenames & assigns n to the multiplier variable
    char *infile = argv[1];
    #define buffersize 512

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

	 // create buffer
    unsigned char buffer[buffersize];

    // filename counter
    int filecount = 0;

    FILE* recoveredjpg = NULL;

    // check if there is a new jpg to write 0 is false
    int newjpg = 0;

    // read through the raw data
    while (fread(buffer, buffersize, 1, inptr) == 1)
    {
        // read first 4 bytes of buffer and see jpg signature is present
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3]) == 0xe0)
        {
            if (newjpg == 1)
            {
                // close previous jps
                fclose(recoveredjpg);
            }
            else
            {
                // new jpg found so continue writing
                newjpg = 1;
            }

            char filename[8];
            sprintf(filename, "%03d.jpg", filecount);
            recoveredjpg = fopen(filename, "a");
            filecount++;
        }

        if (newjpg == 1)
        {
            // write 512 bytes to file
            fwrite(&buffer, buffersize, 1, recoveredjpg);
        }

    }

    // close opened file
    fclose(inptr);
    fclose(recoveredjpg);

    return 0;
}


