import random
import string
from typing import List


def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """

    grid = []
    for _ in range(3):
        grid_line = []

        for _ in range(3):
            grid_line.append(random.choice(string.ascii_uppercase))

        grid.append(grid_line)

    return grid

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """

    words_dict = []

    with open(f, "r") as file:
        for word in file:
            words_dict.append(word.lower())

    return []

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """

    words = []
    while True:
        try:
            word = input()
            words.append(word)
        except EOFError:
            break

    return words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass


print(get_user_words())
