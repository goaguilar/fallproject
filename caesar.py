from cs50 import get_string
from cs50 import get_int

def main():
    print("plaintext: ")
    plaintext = get_string()
    ciphertext = list(plaintext)

    print("code: ")
    code = get_int()

    for i,plainchar in enumerate(ciphertext):
        ##for lowercase
        if (plainchar >= 'a' and plainchar <= 'z'):
            cipherfunct = (ord(plainchar) + code - 97) % 26 + 97;
            cipherchar = chr(cipherfunct)
            ciphertext[i] = cipherchar
        ##for uppercase
        if (plainchar >= 'A' and plainchar<= 'Z'):
            cipherfunct = (ord(plainchar) + code - 65) % 26 + 65;
            cipherchar = chr(cipherfunct)
            ciphertext[i] = cipherchar
    print("ciphertext:" + "".join(ciphertext))
    return 0
if __name__ == "__main__":
    main()