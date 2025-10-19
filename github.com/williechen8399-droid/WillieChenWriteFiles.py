import os
os.chdir(os.path.dirname(__file__))


# Create Write FIles quiz 



# Asking questions, creating varibles
name = input("What is your name? ")
color = input("What is your favorite color? ")
pet = input("What was your first pet's name? ")
mother = input("What is your mother's maiden name? ")
school = input("Which elementary school did you attend? ")

  # Open file hackme.txt 
with open ("hackme.txt", "a") as file:
    file.write("---- New Item ----\n")
    file.write("Name: " + name + "\n")
    file.write("Your favorite color: " + color + "\n")
    file.write("First pet's name: " + pet + "\n")
    file.write("Mother's maiden name: " + mother + "\n")
    file.write("The Elementary school: " + school + "\n") 
