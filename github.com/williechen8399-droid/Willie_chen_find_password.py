# Find the password for the user 

import crypt

SHADOW = "shadow.txt"   
WORDLIST = "top1000.txt"

# Part 1: Load the user and find hashes
users = {}
for line in open(SHADOW):
    p = line.split(":")
    if len(p) > 1 and p[1] and p[1] not in ("*", "!", "!!"):
        users[p[0]] = p[1].strip()

def salt(h):
    if h.startswith("$"):
        i = h.find("$", 3)
        return (h[:i+1] if i != -1 else h)
    return h[:2]

# Part 2: Try to find the password
found = {}
for guess in (g.strip() for g in open(WORDLIST)):
    if not guess:
        continue
    for u, h in list(users.items()):
        if crypt.crypt(guess, salt(h)) == h:
            print("FOUND:", u, "->", guess)
            found[u] = guess
            users.pop(u)
    if not users:
        break

print("Total cracked:", len(found))