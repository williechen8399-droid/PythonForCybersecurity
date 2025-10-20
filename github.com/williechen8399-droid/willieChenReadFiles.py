# Creating the read files
# This codes read hackme.txt
import os
os.chdir(os.path.dirname(__file__))  

# Open hackme.txt in read mode
with open("hackme.txt", "r") as file:
    data= file.read() 

# Print the successful hacked statement
print("Here is someone to hack - information")
print(data)