from cs50 import get_int

validheight = 0;
while validheight != 1:
    print("Height:")
    h = get_int()
    if h < 0 or h > 23:
        break
    for i in range(h):
        print(" " * (h - i), end="")
        print("#" * (i + 1) + "  "+ "#" * (i + 1))
    validheight = 1
