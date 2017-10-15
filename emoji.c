#include <cs50.h>
#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <cs50.h>
#include <math.h>
#include <string.h>

typedef wchar_t emoji;

emoji get_emoji(string prompt);

int main(void)
{
    // Set locale according to environment variables
    setlocale(LC_ALL, "");

    // Prompt user for code point
    emoji c = get_emoji("Code point: ");

    // Print character
    printf("%lc\n", c);
}

emoji get_emoji(string prompt)
{
    string emojitext = get_string("%s",prompt);
    if(emojitext[0] != 'U' || emojitext[1] != '+'){
        printf("Invalid format please retry");
        return 1;
    }
    int len = strlen(prompt);
    for(int i = 2; i < len; i++){
        if( (emojitext[i] >= 'A' && emojitext[i] <= 'F') || (emojitext[i] >= 'a' && emojitext[i] <='f') || (emojitext[i] >='0' && emojitext[i] <='9'))
            ;
        else{
            printf("Invalid format please retry");
            return 1;
        }
    }
    emojitext[0] = '0';
    emojitext[1] = 'x';

    emoji r = strtol(emojitext,NULL,16);

    return r;
}