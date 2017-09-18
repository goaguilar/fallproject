#include <cs50.h>
#include <stdio.h>
#include <string.h>

int checkInt(string str)
{
    for(int j = 0; j < strlen(str); j++)
    {
        // check if string characters are within the range of numbers

        if( str[j] >= '0' && str[j] <= '9')
            return 1;
    }

    return 0;
}

int main(int argc, char *argv[])
{
    if(argc != 2 || checkInt(argv[1]))
    {
        printf("ERROR, Needs to be 1 argument and not an int\n");
        return 1;
    }

    string plaintext = get_string("plaintext: ");
    string ciphertext = plaintext;
    string codetext = argv[1];
    int code [strlen(codetext)];
    for (int n = 0; n <strlen(codetext);n++)
    {
        //convert Uppercase code to int value
        if (codetext[n] >= 'A' && codetext[n] <= 'Z')
            code[n] = (int) codetext[n] - 65;
        //convert Lowercase code to int value
        if (codetext[n] >= 'a' && codetext[n] <= 'z')
            code[n] = (int) codetext[n] - 97;
    }

    for (int i = 0; i < strlen(ciphertext); i++)
    {
        int plainchar = ciphertext[i];
        //for lower case
        if (ciphertext[i] >= 'a' && ciphertext[i] <= 'z')
        {
            int cipherfunct = (plainchar + code[i%strlen(codetext)] - 97) % 26 + 97;
            char cipherchar = (char) cipherfunct;
            ciphertext[i] = cipherchar;
        }
        //for uppercase
        if (ciphertext[i] >= 'A' && ciphertext[i] <= 'Z')
        {
            int cipherfunct = (plainchar + code[i%strlen(codetext)] - 65) % 26 + 65;
            char cipherchar = (char) cipherfunct;
            ciphertext[i] = cipherchar;
        }
    }
    printf("ciphertext: %s\n", ciphertext);
    return 0;
}