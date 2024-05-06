README: Word Guessing Game

# Description
This program is a simple console-based word guessing game. Users try to guess a randomly selected word by inputting letters. They have 10 attempts to guess the word correctly.

# Features
#Imports
- random: This module is used to randomly select a word from a predefined list of words.

# Function: `play_game()`
This is the main function where the gameplay logic is implemented.

1. Initialization:
   - `words`: A list of possible words from which the game will randomly select one for the player to guess.
   - `word`: A randomly chosen word from the `words` list using `random.choice()`.
   - `guessed`: An empty string used to keep track of the letters that have been guessed by the player.
   - `tries`: An integer set to 10, representing the number of guesses the player has before the game ends.

2. Game Introduction:
   - The function starts by printing a welcome message and instructions, informing the player that they have 10 attempts to guess the word.

3. Gameplay Loop:
   - The game enters a `while` loop that continues as long as `tries` is greater than 0.
   - Within the loop:
     - `show`: A string that is constructed in each iteration to display the current state of the guessed word with underscores (`_`) for unguessed letters and the actual letters for correctly guessed ones.
     - The current state of the word (`show`) is printed to the console.

4. Guess Input:
   - The player is prompted to enter a letter. This input is checked for various conditions:
     - If the guess is already guessed, not a single alphabetical letter, or if multiple characters are entered, the game prints an error message and skips to the next iteration of the loop without reducing the number of tries.

5. Processing the Guess:
   - If the guessed letter is part of the word, the game prints "Good guess!".
     - If all letters in the word have been guessed (checked using the `all()` function), a success message is displayed and the loop breaks.
   - If the guessed letter is not part of the word, the number of tries is decremented by one and a message is printed showing the remaining number of tries.

6. Game Over:
   - If the player exhausts all their tries (`tries == 0`), a game over message is displayed along with the correct word.

 Main Block
- `if __name__ == '__main__':`
  - This conditional ensures that the game starts only if the script is run as the main program, not when imported as a module in another script. It calls the `play_game()` function to start the game.


# How to Run the Game
Follow the on-screen instructions:
The game will start and display a series of underscores representing the letters of the word to be guessed.

You will be prompted to enter a letter. Type a letter and press Enter.
The game will update the display based on your input, showing any correctly guessed letters in their correct positions.

If the guess is incorrect, the number of remaining tries will decrease.
Continue guessing letters until:
You guess the word correctly, or
You run out of tries.

# Ending Game
The game concludes either when you guess the word correctly, or you exhaust your 10 tries.

Upon completion, the game will display the correct word if you didn't guess it.

