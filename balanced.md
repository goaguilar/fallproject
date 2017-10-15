# Fair and Balanced

## Questions

1. Yes, because 16 + 26 = 3 + 39 = 42

2. Yes, because 0 + 0 = 0 + 0 = 0

3.

```c
bool balanced(int array[], int n){
    //assuming array of size 1 or 0 is balanced
    if((n == 0) || (n ==1) )
        return true;
    if(n ==2){
        if(array[0] == array[1])
            return true;
        else
            return false;
    }
    int leftsum = 0;
    int rightsum = 0;

    //for arrays with even amount of elements
    if(n%2 == 0){
        for(int i = 0; i <= ((n-1)/2); i++){
            leftsum += array[i];
            rightsum += array[n-1-i];
        }
        if (leftsum == rightsum)
            return true;
        else
            return false;
    }
    //for arrays with odd amount of elements
    if(n%2 == 1){
        for(int i = 0; i < ((n-1)/2); i++){
            leftsum += array[i];
            rightsum += array[n-1-i];

        }
        if (leftsum == rightsum)
            return true;
        else
            return false;
    }

}
```

## Debrief

1. None

2. 40 minutes
