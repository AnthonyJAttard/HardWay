def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"multiplying {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle foe the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it my hand?")

print("This is my own function.")
print("Area of a square is 12 * 12.")
print("Add to the area above the area of a rectangle 12 * 6.")
print("Now take away 25 from the result.")
print("Divide the result by 2.")

result = divide(subtract(add(multiply(12, 6), multiply(12, 12)), 25), 2)
print(f"The result is {result}.")
