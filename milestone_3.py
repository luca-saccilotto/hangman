# Choose a random word from the list
import random

word_list = ["apple", "banana", "orange", "grapes", "strawberry"]
word = random.choice(word_list)

# Check whether the guess is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Iteratively check if the input is a valid guess
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
