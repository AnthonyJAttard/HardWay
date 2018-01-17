# Import arv object from sys
from sys import argv

# Store the arguments in script and filename variables
script, filename = argv

# Attempt to open() the filename for reading
txt = open(filename)

# Print out the name of the file
print(f"Here's your file {filename}:")
# Print out the content of the file by using the read() function
print(txt.read())
txt.close()

# Prompt for the filename
print("Type the filename again:")
# Set prompt to "> "
file_again = input("> ")

# Open the file
txt_again = open(file_again)

# Print out the contents of the file using read() function
print(txt_again.read())
txt_again.close()
