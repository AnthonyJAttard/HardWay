# Prints first string
print("Mary had a little lamb.")
# Prints string formatted with the word 'snow'
print("Its fleece was white as {}.".format('snow'))
# Prints another string
print("And everywhere that Mary went.")
# Prints the period ten times on one line
print("." * 10)  # What'd that do?

# Create ten variables end1..end12, each with one character
# from the words Cheese Burger
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Whatch that comma at the end. Try removing it to see what happens
# Prints each variables end1 to end 6 concatinated, ending with a single space
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# Then prints the variables end7 to end12 concatinated
print(end7 + end8 + end9 + end10 + end11 + end12)
