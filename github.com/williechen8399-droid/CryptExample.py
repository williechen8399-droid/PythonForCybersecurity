# Script that encrypts and decrypts text using cryptography module

from cryptography.fernet import Fernet
# Create functions
# Fernet create key
def fernet_create_key():
    key= Fernet.grenerate_key()
    return key
# fErnet Encrypt
def fernet_encrypt(key, plain_text):
    key_b = key.encode()
    plain_text_b = plain_text.encode()
    cipher_text_b = Fernet( key_b).encrypt(plain_text_b)
    return cipher_text_b
# Fernet Decrypt
def fernet_decrypt(key, cipher_text):
    key_b =key.encode()
    cipher_text_b = cipher_text.encode()
    plain_text_b = Fernet(key_b).decrypt(cipher_text_b)
    return plain_text_b
# Ask what to do
print("*" * 40)
print("Welcome to Fernet encryption")
print("This script can create keys, encrypt, or decrypt")
task = input("What would you like to do (c/e/d)?")[0].lower()
# If encrypt
if task == "e":
    # Get key and data
    enc_key = input("What is the key: ")
    plain_text =input("What is the message: ")

    # Call encrypt function
    cipher_text_b = fernet_encrypt(enc_key, plain_text)
    # print out results
    print(" Your encrypted message is")
    print(f"'{cipher_text_b.decode()}'")
# If decrypt
elif task =="d":
    # Ask for text# Get key and data
    enc_key= input("What is the key: ")
    cipher_text = input('What is the encrypted message: ')
    # Call decrypt function
    plain_text_b = fernet_decrypt(enc_key, cipher_text)
    #   print out results
    print(" Your decrypted message is")
    print(f"'{plain_text_b.decode()}'")
# If Create key
elif task =="c":
    enc_key_b = fernet_create_key()
    # Call create function
    # print out results
    enc_key = enc_key_b.decode()
    print(f"Encryption key {enc_key}")
else:
    print("Please anser c/e/d") 