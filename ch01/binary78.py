######################################################################
# Name: Robert Brown
# Program: binary.py
# Description: 7,8,7,8,7...for cybertorm
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

c = 0
while(c < len(binary)):
	decode(binary[c:c+7], 7)
	c = c + 7

	decode(binary[c:c+8], 8)
	c = c + 8

print("")
