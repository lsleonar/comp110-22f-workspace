"""EX03- Wordle - 3rd time around now using functions."""


__author__ = "730621513"


def contains_char(word: str, character: str) -> bool:
    """Given word and a character will compare matches returns True or False."""
    assert len(character) == 1
    indices: int = 0
    
    matches: bool = False
    while not matches and indices < len(word):
        if word[indices] == character:
            matches = True
        else:
            indices += 1
    if matches: 
        return True 
    else: 
        return False


def emojified(word1: str, word2: str) -> str: 
    """Given parameters will print colored blocks of emojis corresponding to wordle parameters returns emojis."""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    assert len(word1) == len(word2)
    index = 0 
    while index < len(word1):
        if word1[index] == word2[index]:
            emoji += GREEN_BOX
        elif contains_char(word2, word1[index]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        index += 1
    return emoji


def input_guess(length: int) -> str:
    """Input of guess word and ensures length is the same as the secret word returns guess word."""
    guess: str = (input(f" Enter a {length} character word: "))
    while length != len(guess):
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def main() -> None:
    """Puts together all the functions creating a wannabe wordle and codes for print statement if you win/ loose."""
    tries = 0
    secret: str = "codes"
    matches = False
    while not matches and tries < 6:
        tries += 1
        print(f"=== Turn {tries}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(secret, guess))
        if guess == secret:
            matches = True
    if matches is True:
        print(f"You won in {tries}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()