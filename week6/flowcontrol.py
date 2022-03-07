#! /usr/bin/env python3
#[Lab-Python] Flow Control
#Christian Gonzalez

print("""You enter a dark room with three doors.
Do you go through door #1, door #2 or door #3?""")

door = input("-> ")

# == Door Number 1 logic ========================================
if door == "1":
    print("There is an Endermen here holding a grass block.")
    print("What do you do?\n")

    print("1. Take the grass block.")
    print("2. Stare at the Endermen.")

    # == Endermen logic =========================================
    endermen = input("-> ")
    
    if endermen == "1":
        print("1) The Endermen robs you. Good job!")
    elif endermen == "2":
        print("2) The Endermen attacks you. Good job!")
    else:
        print(f"N) Well, doing {endermen} is probably better.")
        print("Endermen teleports away.")
# == Door Number 2 logic ========================================
elif door == "2":
    print("You are surrounded by wild wolves")
    print("What do you do?\n")

    print("1. Tame wolves.")
    print("2. Scare wolves away.")

    # == Wolves logic ===========================================
    wolves = input("-> ")

    if wolves == "1":
        print("1) Not enough bones. Good job!")
    elif wolves == "2":
        print("2)The wolves attacks you. Good job!")
    else:
        print(f"N) Doing {wolves} isn't a bad idea.")
        print("Wolves runs away")
# == Door Number 3 logic =========================================
elif door == "3":
    print("There is a creeper walking towards you.")
    print("What do you do?\n")

    print("1. Run away.")
    print("2. Attack.")

    # == Creeper logic ==========================================
    creeper = input("-> ")

    if creeper == "1":
        print("1) You trip and fall into a cave. Good job!")
    elif creeper == "2":
        print("2) Creeper blows you up. Good job!")
    else:
        print(f"{creeper} was a bad idea")
        print(f"You fall into lava")

else:
    print("You are attacked by a baby zombie riding a chicken. Good job!")
