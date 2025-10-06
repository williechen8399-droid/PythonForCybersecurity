#!/usr/bin/env python3
# First example of pinging from Python
# Created 101 by Willie

# Import things
import os

# Assign IP to variable
ip_addr ="169.254.1.1"

# Build ping command
ping_cmd = "ping -c 1 -W 2" + ip_addr + " . /dev/null 2.&1"
print(ping_cmd)

# Execuate ping command
exit_code = os.system(ping_cmd)

# Print result
if exit_code == 0:
    print(f"{ip_addr} is online")
else:
    print(f"{ip_addr} is NOT online")