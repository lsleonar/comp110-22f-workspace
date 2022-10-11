"""EX01 - Chardle excercise - wannabe Wordle."""


__author__ = "730621513"


"""Asks user to input 5-character word and if it is not a 5 character word the 
program prints an error message and the program ends"""
guess: str = (input("Enter a 5-character word:"))
if len(guess) != 5:
    print("Error: Word must contain 5-characters")
    exit()


"""Asks user to input a single character and if it is not a single chracter the 
program prints an error message and the program ends"""
char: str = (input("Enter a single charcter: "))
if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()


'''If user inputs a single character like they are instructed the message searching
 for character in the word they inputted prints'''
if len(char) == 1: 
    print("Searching for " + char + " in " + guess)


'''sets variable intances to value of zero'''
instances: int = 0


"""These all compare the inputted character to the inputted 5 character word. 
If there are any matches these lines tell you what index it's at and they count 
for instances of the character in the inputted guess word"""
if char == guess[0]: 
    print(char + " found at index 0")
    instances = instances + int(1)
if char == guess[1]: 
    print(char + " found at index 1")
    instances = instances + int(1)
if char == guess[2]: 
    print(char + " found at index 2")
    instances = instances + int(1)
if char == guess[3]: 
    print(char + " found at index 3")
    instances = instances + int(1)
if char == guess[4]: 
    print(char + " found at index 4")
    instances = instances + int(1)

    
"""All of these lines are boolean statements that depending on if they are true 
or false print a statment about how many instances of the inputted character was
 found in the inputted guess word"""
if instances > int(1):
    print(str(instances) + " instances of " + char + " found in " + guess)
if instances == int(1):
    print("1 instance of " + char + " found in " + guess)
if instances == int(0):
    print("No instances of " + char + " found in " + guess)