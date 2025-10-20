# Create function
def sendMessage():
    for i in range(10):
        print("That is awsome!")


# Get user inpuy

userInput= input("Was today a gooday? (yes/no): ")

# Convert input to lowercase
userInput = userInput.lower()

# Condition statement
if userInput == "yes":
    sendMessage()
elif userInput == "no":
    print("Don't worry, It will get better!")
else: 
    print("Please answer 'yes' or 'no'.")
