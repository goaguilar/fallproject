# Emoji

## Questions

1. 4-byte

2. A char is only 1 bytes, and a jack-o-lantern needs 4

3.

```c
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
```

## Debrief

1. Past psets

2. 1 hr 45 minutes
