# Import argv
from sys import argv

# type cast input ti integers
print("How old are you?", end=' ')
age = int(input())
print("How tall are you?", end=' ')
# Add input for weight
height = int(input())
print("How much do you weigh?", end=' ')
weight = int(input())

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

# txt = open(filenme) -- correct spelling filename
txt = open(filename)

print(f"Here's your file {filename}:")
# print(tx.read()) -- correct spelling txt
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

# print(txt_again_read())
print(txt_again.read())

# escape \'
print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with '
      '\\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Add closing and starting double quotes
print("--------------")
print(poem)
print("--------------")

# Added parenthesis
five = 10 - (2 + 3)
print(f"This should be five: {five}")


# Add colon, renamed internal variables, fixed math
def secret_formula(started):
    jelly_beans = started * 500
    num_jars = jelly_beans / 1000
    num_crates = num_jars / 100
    return jelly_beans, num_jars, num_crates


start_point = 10000
# Added crates to variables
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
# rename secretformula to secret_formula
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
#  Rename to cats
cats = 30
dogs = 15

# Added parenthesis, colon and fixed logic
if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

# Fixed colons and logic
if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
