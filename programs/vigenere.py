######################################################################
# Name: Robert Brown
# Date: 3/29/2020
# Last Modified: 3/29/2020
# Program: vigenere.py
# Description: Encrpyt or decrpyt with the vigenere cipher and a given
# cipher key
######################################################################

from sys import stdin, argv

def encrypt(plainText, key):
    cipherText = ""
    key = key.replace(" ", "") # remove spaces from key

    j = 0 # counter for key
    for i in range(len(plainText)):
        c = plainText[i]
        if c.isalpha():
            k = ord(key[j].upper())
            j = (j + 1) % len(key)

            if(c.isupper()): # upper case alpha
                x = 65 + ((ord(c) + k) % 26)
            elif(c.islower()): # lower case alpha
                x = 97 + ((ord(c) + k + 20) % 26) # the +20 is to take care of the lowercase and such

            cipherText += chr(x)
        else: # not an alpha char
            cipherText += c

    return cipherText

def decrypt(cipherText, key):
    plainText = ""
    key = key.replace(" ", "") # remove spaces from key

    j = 0 # counter for key
    for i in range(len(cipherText)):
        c = cipherText[i]
        if c.isalpha():
            k = ord(key[j].upper())
            j = (j + 1) % len(key)

            if(c.isupper()): # upper case alpha
                x = 65 + ((ord(c) - k) % 26)
            elif(c.islower()): # lower case alpha
                x = 97 + ((ord(c) - k + 20) % 26) # the +20 is to take care of the lowercase and such

            plainText += chr(x)
        else: # not an alpha char
            plainText += c

    return plainText

####################### Main Program ##################################
mode = argv[1]
key = argv[2]

while(True):
    try:
        text = input()
    except: # placed this here so the program can gracefully take input from a file, otherwise there is an EOFError
        break

    if(mode == "-e"):
        cipherText = encrypt(text, key)
        print(cipherText)
    elif(mode == "-d"):
        plainText = decrypt(text, key)
        print(plainText)

