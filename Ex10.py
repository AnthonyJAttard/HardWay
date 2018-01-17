tabby_cat = '\tI\'m tabbed in.'
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ \"a\" \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

number = 12.34

print(f"{fat_cat} \n{tabby_cat} \n{backslash_cat} \n{persian_cat}")
print("{:d}".format(round(number)))
