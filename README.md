# Questions

## What's `stdint.h`?

It is a header file that declares data types with exact widths. It defines macros that specifies the limits of each type.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Aliases for C/C++ primitive data types:
    uint8_t is for an unsigned 8-bit integer which frees up the first bit and ranges from 0 to 255
    uint62_t is for an unsigned 16-bit integer which frees up the first bit and ranges from 0 to 65535
    unint32 is for an unsigned 32-bit integer which frees up the first bit and ranges from 0 to 4294967295
    int 32 is for a signed 32-bit integer whose first bit is the signing bit and ranges from  –2147483648 to 2147483647

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

A BYTE is 8 bits or 1 byte
A DWORD is 32 bits or 4 bytes
A LONG is 32 bits or 4 bytes
A WORD is 16 bits or 2 bytes

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

BM

## What's the difference between `bfSize` and `biSize`?

bfSize is the size of the entire file, while biSize is the number of bytes required by the image

## What does it mean if `biHeight` is negative?

It means that the image starts from the top and builds down, usually starting with the upperleft corner

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

fopen might return NULL if inptr, which is the address of file 1, is NULL

## Why is the third argument to `fread` always `1` in our code?

Because there is only 1 element to be read

## What value does line 65 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

1

## What does `fseek` do?

Sets the file position of the stream to the padding

## What is `SEEK_CUR`?

The current position of the file pointer