import random

def play_game():
    words = ['trash', 'apple', 'soccer', 'time', 'creative', 'awesome', 'bottle',
              'successful', 'neat', 'interested','story', 'cup,','attention', 'shift', 'delete', 'return', 'okay']
    word = random.choice(words)
    guessed = ''
    tries = 10
    
    print("Welcome to the Word Guessing Game!")
    print("Guess the word, you have 10 attempts.")
    print("Good Luck!!")

    while tries > 0:
        show = ''
        for letter in word:
            if letter in guessed:
                show += letter
            else:
                show += '_'
        print(show)

        guess = input("Enter a letter: ")

        if guess in guessed or not guess.isalpha() or len(guess) != 1:
            print("Invalid input, enter a single alphabetical letter.")
            continue

        guessed += guess

        if guess in word:
            print("Good guess!")
            if all(letter in guessed for letter in word):
                print("You got it! The word was: " + word)
                break
        else:
            tries -= 1
            print("Nope! You have " + str(tries) + " tries left.")

        if tries == 0:
            print("Oh no! Game over! The word was: " + word)

if __name__ == '__main__':
    play_game()
