"""Create your own adventure - Which Teletubby are you?"""


__author__ = "730621513"


player: str = "name"
points: int = 0 
r: int = 0
y: int = 0
g: int = 0
p: int = 0
RED_CIRCLE: str = u"\U0001F534"
YELLOW_CIRCLE: str = u"\U0001F7E1"
GREEN_CIRCLE: str = u"\U0001F7E2"
PURPLE_CIRCLE: str = u"\U0001F7E3"
        

def greet() -> None:
    """Greets player."""
    global player
    player = (str(input("Welcome to the Which Teletubby are you quiz! What is your name?\n")))
    print(f"Hello, {player} please input your answer as a number corresponding to your answer choice")


def question_one(points: int) -> int:
    """Asks player first question adds adventure point."""
    global r
    global y
    global g
    global p
    global player

    answer: int = (int(input("\nWhich trait describes you most?\n1. Cute\n2. Energetic\n3. Fun\n4. Leader\n\n")))

    while answer != 1 and answer != 2 and answer != 3 and answer != 4:
        answer = (int(input("that's not an answer! Try again.")))
    if answer == 1:
        r += 1
        return r
    if answer == 2:
        y += 1
        return y
    if answer == 3:
        g += 1
        return g
    if answer == 4:
        p += 1
        return p

    points += 1
    return points


def question_two() -> int:
    """Asks player second question adds adventure point."""
    global r
    global y
    global g
    global p
    global player
    global points
    answer: int = (int(input(f"\nWhat is your favorite color?\n1. {RED_CIRCLE}\n2. {YELLOW_CIRCLE}\n3. {GREEN_CIRCLE}\n4. {PURPLE_CIRCLE}\n\n")))
    while answer != 1 and answer != 2 and answer != 3 and answer != 4:
        answer = (int(input("that's not an answer! Try again.")))
    if answer == 1:
        r += 1
        return r
    if answer == 2:
        y += 1
        return y
    if answer == 3:
        g += 1
        return g
    if answer == 4:
        p += 1
        return p
    else:
        print("that's not an answer! Try again.")
    points += 1
    return points


def question_three() -> int:
    """Asks player third question adds adventure point."""
    global r
    global y
    global g
    global p
    global player
    global points
    answer: int = (int(input("\nPick your favorite out of these??\n1. Martial Arts\n2. Singing\n3. Funky / Groovy Music\n4. Dreaming\n\n")))

    while answer != 1 and answer != 2 and answer != 3 and answer != 4:
        answer = (int(input("that's not an answer! Try again.")))
    if answer == 1:
        r += 1
        return r
    if answer == 2:
        y += 1
        return y
    if answer == 3:
        g += 1
        return g
    if answer == 4:
        p += 1
        return p
    else:
        print("that's not an answer! Try again.")
    points += 1
    return points
    

def question_four() -> int:
    """Asks player fourth question adds adventure point."""
    global r
    global y
    global g
    global p
    global player
    global points
    points = 4
    answer: int = (int(input("\nPick a Dance Move:\n1. Star Jump\n2. a twirl\n3. a wiggle\n4. Acting out the song\n\n")))
    while answer != 1 and answer != 2 and answer != 3 and answer != 4:
        answer = (int(input("that's not an answer! Try again.")))
    if answer == 1:
        r += 1
        return r
    if answer == 2:
        y += 1
        return y
    if answer == 3:
        g += 1
        return g
    if answer == 4:
        p += 1
        return p
    else:
        print("that's not an answer! Try again.")
    points += 1
    return points


def more_info() -> None:
    """Gives player information on quiz."""
    print("This quiz compares your personality with each of the Teletubbies personalities to tell you which Teletubby you are.")


def main() -> None:
    """Incoporates all the functions and makes start screen."""
    global r
    global y
    global g
    global p
    global points
    global player
    greet()
    choice = (int(input("\n1. Start quiz\n2. More info\n3. Quit\n\n")))
    if choice == 2:
        more_info()
    if choice == 3:
        print(f"You have accumulated {points} adventure points")
        quit()
    if choice == 1 and points == 0:
        question_one(0)
        question_two()
        question_three()
        question_four()
        if r >= y and r >= g and r >= p:
            print(f"\n{player} you are Po the red Teletubby!")
        if y > r and y >= g and y >= p:
            print(f"\n{player} you are Laa- Laa the yellow Teletubby!")
        if g > r and g > y and g >= p:
            print(f"\n{player} you are Dipsy the green Teletubby!")
        if p > y and p > g and p > r:
            print(f"\n{player} you are Tinky Winky the purple Teletubby!")
        print(f"{player} you have accumulated {points} adventure points")


if __name__ == "__main__":
    main()
