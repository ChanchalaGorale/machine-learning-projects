import random
import time

HANGMAN_PICS = [
    """
       _____
      |
      |
      |
      |
      |
      |
    __|__
    """,
    """
       _____
      |     |
      |     |
      |
      |
      |
      |
    __|__
    """,
    """
       _____
      |     |
      |     |
      |     |
      |
      |
      |
    __|__
    """,
    """
       _____
      |     |
      |     |
      |     |
      |     O
      |
      |
    __|__
    """,
    """
       _____
      |     |
      |     |
      |     |
      |     O
      |    /|\\
      |    /
    __|__
    """,
    """
       _____
      |     |
      |     |
      |     |
      |     O
      |    /|\\
      |    / \\
    __|__
    """
]

WORD_LIST = ["january", "border", "film", "promise", "kids", "lungs", "doll"]
MAX_TRIES = len(HANGMAN_PICS) - 1

def get_valid_guess(already_guessed):
    while True:
        guess = input("Enter your guess (single letter): ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single letter.")
        elif guess in already_guessed:
            print("🔁 You already guessed that letter.")
        else:
            return guess

def display_word(word, guessed_letters):
    return ''.join([ch if ch in guessed_letters else '*' for ch in word])

def play_game():
    word = random.choice(WORD_LIST)
    guessed_letters = set()
    wrong_guesses = 0

    print("\n🔤 The game is about to start! Let's play Hangman!")
    time.sleep(1)

    while wrong_guesses < MAX_TRIES:
        current_display = display_word(word, guessed_letters)
        print(f"\nWord: {current_display}")
        print(HANGMAN_PICS[wrong_guesses])

        if current_display == word:
            print("🎉 Congrats! You've guessed the word correctly!")
            break

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            wrong_guesses += 1
            print(f"❌ Wrong guess. You have {MAX_TRIES - wrong_guesses} tries left.")

    else:
        print(HANGMAN_PICS[wrong_guesses])
        print(f"💀 You're hanged! The word was: {word}")

def main():
    print("\n👋 Welcome to the Hangman game!")
    name = input("Enter your name: ").strip()
    print(f'Hello {name}! Best of luck!')
    time.sleep(1)

    while True:
        play_game()
        again = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for playing! See you next time.")
            break

if __name__ == "__main__":
    main()
