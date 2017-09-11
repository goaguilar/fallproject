#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int validheight = 0;
    while(validheight != 1){
        int h = get_int("Height: ");
        if(h >= 0 && h <= 23){
            for(int i = 0;i <= h-1; i++){
                for(int j = 0; j <h-i-1;j++)
                    printf(" ");
                for(int k = 0; k <= i; k++)
                    printf("#");
                printf("  ");
                for(int l = 0; l <= i; l++)
                    printf("#");
                printf("\n");
            }
            validheight = 1;
        }
    }

}