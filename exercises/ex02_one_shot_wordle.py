"""Ex 02 One Shot Wordle - Wannabe wordle!"""

__author__ = "730621513"

# These following lines set what the variables equal 
secret: str = "python"

guess: str = (input(f"What is your {len(secret)} -letter guess? "))

emoji: str = ""

index: int = 0

# These following lines allow the unicode to be simplied 
# and associated with the emoji they represent
WHITE_BOX: str = "\U00002B1C"

GREEN_BOX: str = "\U0001F7E9"

YELLOW_BOX: str = "\U0001F7E8"

# This while statement allows the user to try again if the length 
# of their word is not the same length as secret
while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

# This section of code checks to see if any letters in the guess word
# match the secret word in the same index and if it does it puts a green block in its place
while index < len(guess):
    if guess[index] == secret[index]:
        emoji += GREEN_BOX
# This following section of code checks to see if any letters in the guess word
# match the secret word at any index and then codes for yellow boxes to be put there
    if guess[index] != secret[index]:
        matches: bool = False
        indices: int = 0
        while not matches and indices < len(secret):
            if secret[indices] == guess[index]:
                matches = True
            else:
                indices += 1
        if matches: 
            emoji += YELLOW_BOX
# This following section of code will add a white box for every letter in the guess word that 
# didn't match any letter in the secret word
        else: 
            emoji += WHITE_BOX
# This line of code help ends the while loop so it doesnt infinitely loop
    index += 1
# These lines of code get the messages that correspond with the results to print
print(emoji)
if guess == secret:
    print("Woo! You got it!")
if guess != secret:
    print("Not quite. Play again soon!")