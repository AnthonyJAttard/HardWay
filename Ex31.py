print("""You enter a dark room with three doors.
Do you go through door #1 or door #2 or door #3""")

door = input("> ")

if door == "1":
    print("There's a giant bear eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats you face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss of Cthulh's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of much.")
        print("Good job!")

elif door == "3":
    print("You see a stair case.")
    print("""Do you go:
(1) Up the stairs? or
(2) Down the stairs?""")

    stairs = input("> ")

    if stairs == "1":
        print("Your are in a strange room, there is a kind of a machine with two levers.")
        print("""Do you:
(1) Pull the first lever? or
(2) Pull the second lever? or
(3) Leave it alone and go back down stairs?""")

        lever = input("> ")

        if lever == "1":
            print("You vanish in a puff of smoke! Goodbye!")
        elif lever == "2":
            print("You receive a massive electrical shock! Goodbye!")
        else:
            print("You go back down stairs and fall through a trap door to you death! Goodbye!")

    elif stairs == "2":
        print("You enter the basement and you are killed by Pennywise the Clown. Now you will float!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
