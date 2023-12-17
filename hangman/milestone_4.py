# Create a new script called milestone_4.py. This file will contain the code for the third milestone.
# Define the __init__ method of the Hangman class.
# Step 1:
# Create a class called Hangman.
# Step 2:
# Inside the class, create an __init__ method to initialise the attributes of the class.
# Pass in word_list and num_lives as parameters. Make num_lives a default parameter and set the value to 5.
import random

class Hangman:
    """
        Initialize the class with a word list and number of lives.
    """
    def __init__(self, word_list, num_lives=5):

# Step 3:
# Initialise the following attributes:
#     word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script
#     word_guessed: list - A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple', 
#     the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
#     num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet
#     num_lives: int - The number of lives the player has at the start of the game.
#     word_list: list - A list of words
#     list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially
        """
        Parameters:
        - word_list (list): A list of words.
        - num_lives - 5 number of lives.
        - word - random selected word from the word_list.
        - word_guessed - 
        """
        self.word_list = word_list
        self.num_lives = 5
        self.word = random.choice(word_list)
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.list_of_guesses = {}