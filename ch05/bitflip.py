######################################################################
# Name: Robert Brown
# Date: 5/8/2020
# Last Modified: 4/21/2020
# Program: xor.py (python3)
# Description: Encrypt or decrpyt a file using the binary XOR method
# Take the key from a binary file of equal length named "key"
######################################################################
import sys
import math 

KEYFILE = "riddle.txt"

key = bytearray()
# read key data as a byte array
with open(KEYFILE, 'rb') as f:
	data = f.read()
	key = bytearray(data)

msg = bytearray()
i = 0

def invertBits(num):
	x = int(math.log2(num)) + 1

	for i in range(x):
		num = (num ^ (1 << i))

	return(num)

for k in key:
	msg.append(invertBits(k))

# Output the byte array message.
sys.stdout.buffer.write(msg)
