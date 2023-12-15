from milestone_2 import ask_user
# Step 1:
# Create a while loop and set the condition to True. Setting the condition to True ensures that the code runs continuously.
# In the body of the loop, write the code required for the following steps.
# Step 2:
# Ask the user to guess a letter and assign this to a variable called guess.
# Step 3:
# Check that the guess is a single alphabetical character. Hint: You can use Python's isalpha method to check if the guess is alphabetical.
# Step 4:
# If the guess passes the checks, break out of the loop.
# Step 5:
# If the guess does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."
# imported from milestone_2
word = ask_user()
print(type(word))

single_word = list(word)

while True:
    guess = input("Please guess the letter: ")
    
    if len(guess) == 1 and guess.isalpha():
        # Added flag in order to move onto the next set of if statements, other was exiting due to break
        valid_guess = True
        break
    else:
        print("Invalid letter. Please enter a single alphabetical character.") 

#Now check if the user has guessed the 'right' letter from the word 
if valid_guess:   
    if guess in single_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry {guess} is not in the word. Try again.")



