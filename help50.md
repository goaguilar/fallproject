# Helping `help50`

## Questions

1. % is a binary expression that only works on integer types. Perhaps you should change the operands and declare them as ints.

2. The type of the variable must match the return type of get_string.

3. You are comparing the value to a character that can only hold a value from -128 to +127. It can never hold the value of 255, consider making
the character unsigned.

4. You are trying to initialize a pointer with a struct initializer. There is no memory set aside for a struct in the pointer.

## Debrief

1. stack overflow and lecture

2. 40 minutes
