# Stack Smashing

## Questions

1. A canary value is a value written just before the return value. If the canary value is rewritten, then that indicates that there is a buffer overflow.

2. It is called that because miners took canaries with them into the mines to serve as a detection of the presence of any dangerous gases. If they died,
then that told the miners to clear the area.

3. #include <string.h>

void foo (char *bar)
{
   char  c[1];

   strcpy(c, bar);
}

int main ()
{
   foo(A0x1010C042);

   return 0;
}

## Debrief

1. Youtube and wikipedia link

2. 25 minutes
