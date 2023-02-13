# Choose a random word from the list
import random

# Create the class
class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_lives = num_lives
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    # Check whether the guess is in the word
    def check_guess(self,guess):
            guess = guess.lower()
            if guess in self.word:
                print(f"Good guess! {guess} is in the word.")
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        self.word_guessed[i] = guess
                self.num_letters -= 1
            else:
                self.num_lives -= 1
                print(f"Sorry, {guess} is not in the word.")
                print(f"You have {self.num_lives} lives left.")            
            self.list_of_guesses.append(guess)

    # Iteratively check if the input is a valid guess
    def ask_for_input(self):
            while True:
                guess = input("Enter a letter: ")
                if len(guess) != 1 or not guess.isalpha():
                    print("Invalid letter. Please, enter a single alphabetical character.")
                elif guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.check_guess(guess)
                    break

# Create a function that will run all the code
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            break

# Call the function to test the code
if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "grapes", "strawberry"]
    play_game(word_list)