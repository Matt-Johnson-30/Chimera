######################################################################
# Name: Robert Brown
# Date: 5/8/2020
# Last Modified: 5/08/2020
# Program: timelock.py (but for challenge 5)
# Description: Modified for challenge 5 (longer secret key)
######################################################################
from datetime import datetime, timedelta
import pytz
from hashlib import md5

DEBUG = True

# Set to True if on the challenge server
ON_SERVER = True

# Valid time interval
INTERVAL = 60

# Current datetime?
#current_utc = datetime.now()
#current = "2017 04 26 15 14 30"
#current = datetime.strptime(current, "%Y %m %d %H %M %S")
current = datetime.now()

#sync with gourds sever
current -= timedelta(0, 3280)


# Get epoch time from stdin
#epoch = input()
epoch = "2001-02-03 04:05:06"
epoch = datetime.strptime(epoch, "%Y-%m-%d %H:%M:%S")

# Convert the times to UTC
zone = pytz.timezone("America/Chicago")
current_utc = current.astimezone(pytz.utc)
epoch = zone.localize(epoch, is_dst=None)
epoch_utc = epoch.astimezone(pytz.utc)

# Calculated elapsed time
elapsed = int((current_utc - epoch_utc).total_seconds())
last_min = elapsed - elapsed % INTERVAL

# get the hash of the hash
hash1 = md5(str(last_min).encode()).hexdigest()
hash = md5(str(hash1).encode()).hexdigest()

code = ""
# get first two alpha characters from hash
for h in hash:
	if len(code) is 2:
		break

	if h.isalpha():
		code += h

# get last two numeric characters from hash
for h in reversed(hash):
    if len(code) is 4:
        break

    if h.isnumeric():
        code += h

# get the middle char of the hash
code += hash[int(len(hash)/2) - 1]
code += hash[int(len(hash)/2)]

if DEBUG:
	print("Current (UTC): " + str(current_utc))
	print("Epoch (UTC): " + str(epoch_utc))
	print("Elapsed: " + str(elapsed))
	print("Last min: " + str(last_min))
	print("MD5: " + hash)

print(code)
