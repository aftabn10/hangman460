import random

class Hangman:
    """
    This class is used to setup the Hangman Game.
    """
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the class with a word list and number of lives with a default value of 5.
        
        Parameters:
        - word_list (list): A list of words.
        - num_lives - 5 number of lives.
        - word - random selected word from the word_list.
        - word_guessed - A list of the letters of the word, for each letter not yet guessed show '_'. This is multiplied by the length of the word.
        - num_letters - The (int) number of UNIQUE letters in the word that have not been guessed yet. Also used set to only count UNIQUE letters.
        - list of guesses - A list of guesses that have been tried. Initially set as an empty list.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = '_' * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        This function is used to check the players guess for the word.

        Args:
            guess is what gets passed as the value from the player.
        Returns:
            If guess is in the word, then get a positive message, otherwise get asked to try again and you lose a life.
        """
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left")

        for i in range(len(self.word)):
            if self.word[i] == guess:
        # Replace the corresponding "_" in the word_guessed with the guess
                word_guessed_list = list(self.word_guessed)
                word_guessed_list[i] = guess
                self.word_guessed = ''.join(word_guessed_list)
                self.num_letters -= 1
        
    def ask_for_input(self):
        """
        This function is used to ask for an input from the player.

        Returns:
            If conditions are not met, then will print a message to the player.
            If conditions are met but its a guess that already exists in the list of guesses then will let the player know.
            If conditions are met then will run the check_guess function and pass the guess variable and also append the value to the list of guesses.
        """
        print(self.word_guessed)
        guess = input ("Please guess a letter: ")

        # Used 'or not' to print if either condition is True 
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess) 

def play_game(word_list):
    """
    This function is used to play the Hangman game.

    Args:
        word_list (list): A list of word for the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

# Specify the word list
word_list = ['apple', 'grapes', 'pineapple', 'oranges', 'peaches']

# Call the play_game function and pass the word_list
play_game(word_list)