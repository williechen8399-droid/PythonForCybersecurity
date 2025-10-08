#!/usr/bin/env python3
# First example of pinging from Python
# Created 101 by Willie

# Import things
import os
import platform
# Assign IP to variable
ip_addr ="127.0.0.1"

# Find current OS
current_os = platform.system().lower()
# If Windows
if current_os == "windows":
    ping_cmd = ""
else:
    ping_cmd = "ping -c 1 -w 2" + ip_addr + " > nul"

print(ping_cmd)
# Build ping command

print(ping_cmd)

# Execuate ping command
exit_code = os.system(ping_cmd)

# Print result
if exit_code == 0:
    print(f"{ip_addr} is online")
else:
    print(f"{ip_addr} is NOT online")


# ping -n 1 -w 2 8.8.8.8 > NUL