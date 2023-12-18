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
    This class is used to setup the Hangman Game.
    """
    def __init__(self, word_list, num_lives=5):
        """
        Initialize the class with a word list and number of lives with a default value of 5.
        """  
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

# (Task2) Define a method called check_guess. Pass the guess to the method as a parameter. 
# In the body of the method, write the code for the following steps:

# Convert the guessed letter to lower case
# Create an if statement that checks if the guess is in the word
# In the body of the if statement, print a message saying "Good guess! {guess} is in the word."

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

# (Task3) Return to your check_guess method and extend it to replace the underscore(s) in the word_guessed with the letter guessed by the user.

# In the if block of your check_guess method, after your print statement, do the following:

# Create a for-loop that will loop through each letter in the word
# Within the for-loop, do the following:
# Create an if statement that checks if the letter is equal to the guess
# In the if block, replace the corresponding "_" in the word_guessed with the guess. 
# HINT: You can index the word_guessed at the position of the letter and assign it to the letter
# Outside the for-loop, reduce the variable num_letters by 1

        for i in range(len(self.word)):
            if self.word[i] == guess:
        # Replace the corresponding "_" in the word_guessed with the guess
                word_guessed_list = list(self.word_guessed)
                word_guessed_list[i] = guess
                self.word_guessed = ''.join(word_guessed_list)
                self.num_letters -= 1

# (Task2)Define a method called ask_for_input. In the body of the method, do the following:

# Create a while loop and set the condition to True
# Ask the user to guess a letter and assign this to a variable called guess
# Create an if statement that runs if the guess is NOT a single alphabetical character
# In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."
# Create an elif statement that checks if the guess is already in the list_of_guesses
# In the body of the elif statement, print a message saying "You already tried that letter!"

# If the guess is a single alphabetical character and it's not already in the list_of_guesses, 
# create an else block and call the check_guess method. 
# Remember to pass the guess as an argument to this method.

# Finally, append the guess to the list_of_guesses.
# Ensure you do this in the else block of this function, rather than inside the check_guess method, 
# so that the letter can be appended to the list_of_guesses in both conditions.

    def ask_for_input(self):
        """
        This function is used to ask for an input from the player.

        Returns:
            If conditions are not met, then will print a message to the player.
            If conditions are met but its a guess that already exists in the list of guesses then will let the player know.
            If conditions are met then will run the check_guess function and pass the guess variable and also append the value to the list of guesses.
        """
        print(self.word)
        guess = input ("Please guess a letter: ")

        # Used 'or not' to print if either condition is True 
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess) 

game_instance = Hangman(["apple", "banana", "orange"])  # Example usage
game_instance.ask_for_input()