#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT 13

# Get message from user
message = input("What is the message: ")
message = message.upper()
finalMessage = ""

# For each letter in message 
for letter in message:
    # convert letter to number
    convertedLetter = ord(letter)

    # Check for letter
    if convertedLetter >= 65 and convertedLetter <= 90:
        #Add 13 to number
        convertedLetter += 13
        #   Past Z?   
        if convertedLetter > 90:
            # Subtract 26 from number
            convertedLetter -= 26
        # Convert number to letter
        uptLetter = chr(convertedLetter)
        finalMessage += uptLetter
    else: 
        finalMessage += letter
# Print updated message
print(finalMessage)