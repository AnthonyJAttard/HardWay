

def loop(repeat, increment):
    for i in range(0, repeat, increment):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


numbers = []
num = int(input("How many times to loop: "))
inc = int(input("Increment by: "))
loop(num, inc)

print("The numbers: ")

for number in numbers:
    print(number)
