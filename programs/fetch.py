######################################################################
# Name: Robert Brown
# Date: 3/31/2020
# Last Modified: 4/2/2020
# Program: fetch.py (run using python3)
# Description: Read contents in an FTP directory and decode a covert
# message from the permissions of the files. There program can decode
# either 7 or 10 bits per line depending on the mode
######################################################################
from ftplib import FTP

IP = "jeangourd.com"
#IP = "192.168.1.9"
PORT = 21
FOLDER = "7" # Folder to scan the contents of
MODE = "7" # Mode is either a 7 or 10

bitsPerByte = 7 # typically either 7 or 8

################# Helper Functions ######################
# decode a binary string with given bits per byte
def decodeBinary(binary, bits):
    for i in range(0,len(binary), bits):
        byte = binary[i:i+bits] # get the current slice of bits
        num = int(byte, 2) # convert that slice to a num
        if num == 8: # backspace
            print('\b' + ' ' + '\b',end="")
        else: # otherwise, just print the char
            print(chr(num), end="")

# fetch contents from an FTP server while
# logged in as an anonymous
def fetch(ip, port, folder):
    contents = []
    ftp = FTP()
    ftp.connect(ip, port)
    ftp.login() # login as anonymous
    ftp.cwd(folder)
    ftp.dir(contents.append)
    ftp.quit()

    return contents

# Scan the retreived contents for a covert message to read
def covertRead(contents, mode):
    binary = ""

    for c in contents:
        # Get the appropriate slice of permisison bits based on the mode
        if c[0:3] == "---" and mode == "7":
            bits = c[3:10]
        elif mode == "10":
            bits = c[0:10]
        else:
            continue

        # Change the file permission to 0's and 1's
        for b in bits:
            if b == '-':
                binary += "0";
            else:
                binary += "1";

    # Once all the contents as been scanned, decode the message
    decodeBinary(binary, bitsPerByte)
    print("")

#################### Main Program ############################
contents = fetch(IP, PORT, FOLDER)
covertRead(contents, MODE)
