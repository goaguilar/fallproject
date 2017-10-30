from cs50 import get_int

sum1 = 0
sum2 = 0

print("Number: ")
card = get_int()
tempcard1 = card
tempcard2 = card//10

while tempcard1> 0:
    sum1 += tempcard1%10
    tempcard1 //= 100

while tempcard2>0:
    if ((tempcard2 % 10) *2 > 9 ):
        sum2 += ((tempcard2 % 10)*2) // 10
        sum2 += ((tempcard2 % 10)*2) % 10
    else:
        sum2 += (tempcard2%10)*2
    tempcard2 //= 100
sumtotal = sum1 + sum2
if(sumtotal%10 == 0):
    if((card >= 340000000000000 and card < 350000000000000) or (card >= 370000000000000 and card < 380000000000000)):
        print("AMEX\n")
    elif(card >= 5100000000000000 and card < 5600000000000000):
        print("MASTERCARD\n")
    elif((card >= 4000000000000 and card < 5000000000000) or (card >= 4000000000000000 and card < 5000000000000000)):
            print("VISA\n")
else:
    print("INVALID")