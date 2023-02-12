# Define the list of possible words
word_list = ["apple", "banana", "orange", "grapes", "strawberry"]
print(word_list)

# Choose a random word from the list
import random

word = random.choice(word_list)
print(word)

# Ask the user for an input
guess = input("Guess a letter: ")

# Check that the input is a single character
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
