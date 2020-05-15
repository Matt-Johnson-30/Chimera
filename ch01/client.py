######################################################################
# Name: Robert Brown
# Date: 4/24/2020
# Last Modified: 4/20/20
# Program: client.py (run using python3)
# Description: Connect to a chat server and receive a message char by
# char. Time the delay between those chars and translate that to
# either a 0 or 1 to unveal a covert message.
# Tested with a local server modeled after the example code.
######################################################################

import socket
from sys import stdout
from time import time

# enables debugging output
DEBUG = True

ZERO = .2
ONE = .1

# set the server's IP address and port
#ip = "localhost"
#port = 1337
ip = "138.47.99.163"
port = 12321

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

print("\n[Connected to the chat server]\n")
msg = ""

# receive data until EOF
covert_bin = ""
data = s.recv(4096).decode()
while (data.rstrip("\n")[-3:] != "EOF"):
    # output the data
    stdout.write(data)
    stdout.flush()
    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()
    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)
	# ignore the .15 timing
    if(delta < .16 and delta > .14):
        msg+="(.15)"
	# Map the delay to either a zero or one
    elif(delta >= (ONE + ZERO)/2):
        msg+="(.2)"
        covert_bin += '1'
    else:
        msg+="(.1)"
        covert_bin += '0'

	# Print the delay with the received char
    if (DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

# close the connection to the server
s.close()

print("[Disconected from chat server]")

# convert received data
covert = ""
i = 0
while i < len(covert_bin):
    byte = covert_bin[i:i+7] # get the current slice of bits
    num = int(byte, 2) # convert that slice to a num
    covert += chr(num)
    i += 8
print("Covert message: " + covert)


print(msg)
