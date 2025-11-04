import random
import string

print("This is a password generator.")

length = int(input("Password length (4-300): "))

if length < 4 or length > 300:
    print("Out of range")
    exit()

# ask what types to use
lower = input("lowercase? y/n: ") == "y"
upper = input("uppercase? y/n: ") == "y"
nums = input("numbers? y/n: ") == "y"
symbols = input("symbols? y/n: ") == "y"
force_letter = input("first letter must be a letter? y/n: ") == "y"
no_similar = input("remove confusing chars (I,l,1,O,0)? y/n: ") == "y"

chars = ""
if lower: chars += string.ascii_lowercase
if upper: chars += string.ascii_uppercase
if nums: chars += string.digits
if symbols: chars += "!@#$%^&*()_-+=[]{};:,.?/"

if no_similar:
    for c in "Il1O0":
        chars = chars.replace(c, "")

if chars == "":
    print("Please select at least one character type.")
    exit()

password = ""

# make first char a to z
if force_letter:
    password += random.choice(string.ascii_letters)
    length -= 1

for i in range(length):
    password += random.choice(chars)

print("Here's your password:", password)
