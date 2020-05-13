#####################################################################
# Name: Robert Brown
# Date: 5/8/2020
# Last Modified: 4/21/2020
# Program: steg.py (python3)
# Description: Either in encrpyt or decrpyt one file inside another
# file using the bit or byte steganography methods
######################################################################
from sys import argv, exit, stdout

BYTE_SIZE = 8

########################### Main Program #############################
oppr = 'r' # either store (s) or retrieve (r)
mode = 'b' # either bit (b) or Byte (B) mode
offset = 0
interval = 1
wrapper_file = ""
hidden_file = ""
direction = 1 # left to right (l) or right to left (r) - being done l8r
wrapper_bytes = bytearray()
hidden_bytes = bytearray()
sentinel = bytearray([0,255,0,0,255,0])

# parse the imput arguments and set the parameters
for i in range(1,len(argv)):
	cmd = argv[i][:2]

	if cmd == "-s":
		oppr = 's'
	elif cmd == "-r":
		oppr = 'r'
	elif cmd == "-b":
		mode = 'b'
	elif cmd == "-B":
		mode = 'B'
	elif cmd == "-o":
		offset = int(argv[i][2:])
	elif cmd == "-i":
		interval =  int(argv[i][2:])
	elif cmd == "-w":
		wrapper_file = argv[i][2:]
	elif cmd == "-h":
		hidden_file = argv[i][2:]
	else:
		print(cmd + " is an invalid argument")
		exit(0)

# read the wrapper file
with open(wrapper_file, 'rb') as f:
	data = f.read()
	wrapper_bytes = bytearray(data)

# read the hidden file if needed
if oppr is 's':
	with open(hidden_file, 'rb') as f:
		data = f.read()
		hidden_bytes = bytearray(data)

# byte method store
if mode is 'B' and oppr is 's':
	# TODO: add a check to ensure the wrapper is large enough

	# first write the data
	for byte in hidden_bytes:
		wrapper_bytes[offset] = byte
		offset += interval

	# then write the sentinel
	for byte in sentinel:
		wrapper_bytes[offset] = byte
		offset += interval

	# print to stdout the updated wrapper
	stdout.buffer.write(wrapper_bytes)
	exit(0)

# byte method retrieve
if mode is 'B' and oppr is 'r':
	while offset < len(wrapper_bytes):
		byte = wrapper_bytes[offset]

		hidden_bytes.append(byte)

		# check if sentinel is found
		if hidden_bytes[-len(sentinel):] == sentinel:
			break

		offset += interval

	# file over or sentinel found
	stdout.buffer.write(hidden_bytes[:-len(sentinel)])
	exit(0)

# bit method store
if mode is 'b' and oppr is 's':
	# Write the data one bit at a time
	for i in range(len(hidden_bytes)):
		for j in range(BYTE_SIZE):
			wrapper_bytes[offset] &= 254
			wrapper_bytes[offset] |= ((hidden_bytes[i] & 128) >> 7)
			hidden_bytes[i] = (hidden_bytes[i] << 1) & (2**BYTE_SIZE-1)
			offset += interval

	# Write the sentinel one bit at a time
	for i in range(len(sentinel)):
		for j in range(BYTE_SIZE):
			wrapper_bytes[offset] &= 254
			wrapper_bytes[offset] |= ((sentinel[i] & 128) >> 7)
			sentinel[i] = (sentinel[i] << 1) & (2**BYTE_SIZE-1)
			offset += interval

	stdout.buffer.write(wrapper_bytes)
	exit(0)

# bit method retrieve
if mode is 'b' and oppr is 'r':
	while offset < len(wrapper_bytes):
		byte = 0

		# build the byte, one bit at a time
		for j in range(BYTE_SIZE):
			byte |= (wrapper_bytes[offset] & 1)

			if j < BYTE_SIZE - 1:
				byte = (byte << 1) & (2 ** BYTE_SIZE - 1)
				offset += interval

		hidden_bytes.append(byte)

		# check if sentinel is found
		if hidden_bytes[-len(sentinel):] == sentinel:
			break

		offset += interval

	# file over or sentinel found
	stdout.buffer.write(hidden_bytes[:-len(sentinel)])
	exit(0)





