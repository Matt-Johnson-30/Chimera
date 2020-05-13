######################################################################
# Name: Robert Brown
# Date: 5/8/2020
# Last Modified: 4/21/2020
# Program: xor.py
# Description:
######################################################################
import sys
KEYFILE = "740cfd3199e2a52a2331528145eab143"
BUFF_SIZE = 4096

key = ""
# read key data
with open(KEYFILE, 'rb') as f:
	data = f.read()
	key = bytearray(data)

msg = bytearray()
i = 0

chunk = sys.stdin.buffer.read(BUFF_SIZE)
while chunk:
	for c in chunk:
		msg.append(c ^ key[i % len(key)])
		i = i + 1

	chunk = sys.stdin.buffer.read(BUFF_SIZE)

sys.stdout.buffer.write(msg)
