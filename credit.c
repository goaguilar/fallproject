#include <cs50.h>
#include <stdio.h>

int main(void)
{

    long long card = get_long_long("Number: ");
    long long tempcard1, tempcard2;
    int sum1 = 0;
    int sum2 = 0;
    int sumtotal = 0;


    for (tempcard1 = card; tempcard1 > 0; tempcard1 /= 100){
        sum1 += (tempcard1 % 10);
    }
    for (tempcard2 = card/10; tempcard2 > 0; tempcard2 /=100){
        if ((tempcard2 % 10) *2 > 9 ){
            sum2 += ((tempcard2 % 10)*2) / 10;
            sum2 += ((tempcard2 % 10)*2) % 10;
        }
        else
            sum2 += (tempcard2 % 10)*2;
    }

    sumtotal = sum1 + sum2;

    if (sumtotal % 10 == 0){
        if((card >= 340000000000000 && card < 350000000000000) || (card >= 370000000000000 && card < 380000000000000) )
            printf("AMEX\n");
        else if(card >= 5100000000000000 && card < 5600000000000000)
            printf("MASTERCARD\n");
        else if((card >= 4000000000000 && card < 5000000000000) || (card >= 4000000000000000 && card < 5000000000000000))
            printf("VISA\n");
    }
    else
        printf("INVALID\n");

    return 0;
}