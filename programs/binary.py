######################################################################
# Name: Robert Brown
# Date: 3/19/2020
# Last Modified: 3/30/2020
# Program: binary.py
# Description: This program takes a file with either 7 or 8 bit ASCII
# binary as input. The program will then convert this binary to text,
# automatically detecting 7 or 8 bit.
######################################################################

##### Helper Functions #####

# Check if a string is binary or not
def checkBinary(str):
    s = set(str)

    if s != {'0','1'} and s != {'0'} and s != {'1'}:
        return False
    else:
        return True

# decode a binary string with given bits per byte
def decode(binary, bits):
    for i in range(0,len(binary), bits):
        byte = binary[i:i+bits] # get the current slice of bits
        num = int(byte, 2) # convert that slice to a num
        if num == 8: # for a backspace, move the cursor back, print over with a space, move the cursor back again
            print('\b' + ' ' + '\b',end="")
        else: # otherwise, just print the char
            print(chr(num), end="")

############################ MAIN CODE #############################
# Get the binary input and and check it
binary = input()
while(not checkBinary(binary)):
    binary = input()

# decode the input
if len(binary) % 7 == 0:
    print("7-bit: ", end="")
    decode(binary, 7)

if len(binary) % 8 == 0:
    print("8-bit: ", end="")
    decode(binary, 8)

print("")
