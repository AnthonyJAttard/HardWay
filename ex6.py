# Declares and defines a variable 'types_of_people'
types_of_people = 10
# Assigns a formatted string to a variable using the above variable
x = f"There are {types_of_people} types of people."  # 1st string in a string

# Declares three variables and assigns to them a string value
# Variable x is a string
binary = "binary"
# Variable do_not is a string
do_not = "don't"
# Variable y combines a string formatted with the above two variables
y = f"Those who know {binary} and those who {do_not}."  # 2nd string in a string

# Print variables x and y
print(x)
print(y)

# Print two strings one with x and one with y
print(f"I said: {x}")  # 3rd string in a string
print(f"I also said: '{y}'")  # 4th string in a string

# Create a boolean variable set to false
hilarious = False
# Create a string variable ready to be formatted
joke_evaluation = "Isn't that joke funny?! {}"
# Print the string formatted with the boolean variable
print(joke_evaluation.format(hilarious))  # Converts boolean to a string, so 5th string in a string

# Create two string variables w and e
w = "This is the left side of..."
e = "a string with a right side."

# Print variables w and e using + for concatenation
print(w + e)
