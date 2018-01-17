from sys import argv

script, filename = argv

print(f"We're going to read {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'r')

print("Reading the file.")
text = target.read()

print("Now to print the text...")
print(text)

print("And finally close it.")
target.close()
