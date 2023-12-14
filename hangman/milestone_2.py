# Hangman Game - Built in Python
import random

# 1.  Define a list of possible word 
# 1.1 Create a list containing the names of my 5 favourite fruits
# 1.2 Assign this list to a variable called word_list
# 1.3 Print out the newly created list 
def ask_user():

    word_list = ['apple', 'grapes', 'pineapple', 'oranges', 'peaches']
    print(word_list)

# 2.  Choose a random word from the list
#     To accomplish this task, you will need to use the 'random' module.
#     The random module is one of Python's built-in modules.
#     It has a choice method which returns a random item from a given sequence.

# 2.1 Go to the first line of your file.
# 2.2 Write import random on the line. Note: To import a module, 
#     you have to use the import keyword at the top of the file.
# 2.3 Create the random.choice method and pass the word_list variable into the choice method.
# 2.4 Assign the randomly generated word to a variable called word.
# 2.5 Print out word to the standard output. Run the code several times 
#     and observe the words printed out after each run.
    word = random.choice(word_list)
    print(word)

# 3.  Ask the user for an input
# 3.1 Using the input function, ask the user to enter a single letter.
# 3.2 Assign the input to a variable called guess.

# 4.  Check that the input is a single character
# 4.1 Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
# 4.2 In the body of the if statement, print a message that says "Good guess!".
# 4.3 Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
# added this code to avoid ask_user script being run twice in case its imported
if __name__ == "__main__":
    ask_user()