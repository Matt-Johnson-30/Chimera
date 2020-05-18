######################################################################
# Name: Robert Brown
# Date: 5/8/2020
# Last Modified: 4/21/2020
# Program: xor.py (python3)
# Description: Encrypt or decrpyt a file using the binary XOR method
# Take the key from a binary file of equal length named "key"
######################################################################
import sys

KEYFILE = "stuff/3d2fad84f4e4a738dff8c58af7bf0742"
BUFF_SIZE = 4096

key = ""
# read key data as a byte array
with open(KEYFILE, 'rb') as f:
	data = f.read()
	key = bytearray(data)

msg = bytearray()
i = 0

# Read a chunk of data from stdin at a time
chunk = sys.stdin.buffer.read(BUFF_SIZE)
while chunk:
	# for each byte in the chunck, bitewise XOR it with
	# the corresponding byte from key[]
	for c in chunk:
		msg.append(c ^ key[i % len(key)])
		i = i + 1

	chunk = sys.stdin.buffer.read(BUFF_SIZE)

# Output the byte array message.
sys.stdout.buffer.write(msg)
