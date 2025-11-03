# Find the password for the user 

import crypt

SHADOW = "shadow.txt"   
WORDLIST = "top1000.txt"

# Part 1: Load the user and find hashes
users = {}
with open("shadow") as f:
    for line in f:
        parts = line.split(":")
        if len(parts) > 1 and parts[1].strip() not in -("", "!", "*"):
            name = parts[0]
            fullHash = parts[1].strip()
            users[name] = fullHash


# Part 2: We need to get salt from hash
def getSalt(h):
    if h.startswith("$"):
        spot = h.find("$", 3)
        if spot != -1:
            return h[:spot+1]
    return h[:2]  

salts = {name: getSalt(h) for name, h in users.items()}     


#Part 3: test out the passwords
for guess in open("top-100.txt"):   
    guess = guess.strip()
    if not guess:
        continue
    for name, fullHash in list(users.items()):
        test = crypt.crypt(guess, salts[name])
        if test == fullHash:
            print("FOUND:", name, "=", guess)
            users.pop(name)
    if not users:
        break