import random

def select_random_word():
    words = ["python", "hangman", "challenge", "openai", "programming", "internship", ""]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = select_random_word()
    guessed_letters = set()
    attempts = 6  # Number of incorrect guesses allowed
    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess: {display_word(word, guessed_letters)}")
        else:
            attempts -= 1
            guessed_letters.add(guess)
            print(f"Wrong guess! Attempts left: {attempts}")
            print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You've guessed the word!")
            break
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()