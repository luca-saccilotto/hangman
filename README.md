# AiCore Scenario - "Hangman" Game

This is an implementation of the "Hangman" game, where the computer thinks of a word and the user tries to guess it. Python and its standard libraries were employed for input/output operations, string manipulation, conditional statements, and loops.

## Milestone 1
In Milestone 1, the focus was on setting up the development environment. This involved installing the necessary tools and libraries required to run the program. A virtual environment was created to keep the dependencies for the project isolated from the other projects on the machine. This step helped to avoid potential conflicts with other projects.

## Milestone 2
In Milestone 2, the goal was to lay the foundation for the program by defining the variables used. This involved creating variables for the word to be guessed, the letters that have been guessed, and the number of guesses left. Careful consideration was given to the data types of the variables to ensure that they would work correctly within the game logic.

## Milestone 3
In Milestone 3, the objective was to create two functions to run the checks. The `check_guess` function takes in the letter that the player has guessed and uses the `in` operator to check if the letter is in the word. The `ask_for_input` function uses a while loop to repeatedly ask the player for input until a valid letter is entered. The loop continues as long as the player has entered an invalid character.

## Milestone 4
In Milestone 4, the program is implemented using a `Hangman` class, with the following methods:
- `__init__` initializes the game with a word and a specified number of lives;
- `ask_for_input` prompts the player to guess a letter and validates the input;
- `check_guess` checks if the guessed letter is in the word, and updates the `word_guessed` list and `num_letters` attribute accordingly.

## Milestone 5
In Milestone 5, the `play_game` function was created to run all the code. It takes in a list of words as an argument and uses it to initialize an instance of the class. Then, the function enters a loop that checks the number of lives the player has left. It continues until either the player has successfully guessed all the letters in the word or the player has run out of lives.
