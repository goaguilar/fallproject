#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if(argc != 2){
        printf("ERROR, Need to input only 1 argument\n");
        return 1;
    }
    string plaintext = get_string("plaintext: ");
    string ciphertext = plaintext;
    int code = atoi(argv[1]);

    for (int i = 0; i < strlen(ciphertext); i++){
        int plainchar = ciphertext[i];
        //for lower case
        if (ciphertext[i] >= 'a' && ciphertext[i] <= 'z')
        {
            int cipherfunct = (plainchar + code - 97) % 26 + 97;
            char cipherchar = (char) cipherfunct;
            ciphertext[i] = cipherchar;
        }
        //for uppercase
        if (ciphertext[i] >= 'A' && ciphertext[i] <= 'Z')
        {
            int cipherfunct = (plainchar + code - 65) % 26 + 65;
            char cipherchar = (char) cipherfunct;
            ciphertext[i] = cipherchar;
        }
    }
    printf("ciphertext: %s\n", ciphertext);
    return 0;
}