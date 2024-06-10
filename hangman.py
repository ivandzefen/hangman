import random
import re

def get_word():
  """
  Selects a random word from a list of words.
  """
  with open('words.txt','r') as f:
      words=f.read()
      words=words.split('\n')
  return random.choice(words).upper()

def display_hangman(wrong_guesses):
    """
    Displays the hangman visual based on the number of wrong guesses.
    """
    stages = [
        r"""
            --------
            |      |
            |
            |
            |
            |
            |
            -------
        """,
        r"""
            --------
            |      |
            |      O
            |
            |
            |
            |
            -------
        """,
        r"""
            --------
            |      |
            |      O
            |      |
            |
            |
            |
            -------
        """,
        r"""
            --------
            |      |
            |      O
            |     /|\
            |
            |
            |
            -------
        """,
        r"""
            --------
            |      |
            |      O
            |     /|\
            |     /
            |
            |
            -------
        """,
        r"""
            --------
            |      |
            |      O
            |     /|\
            |     / \
            |
            |
            -------
        """
    ]
    
    if wrong_guesses==0:
        return  len(stages)
    elif wrong_guesses < len(stages):
        print(stages[wrong_guesses])
    else:
        print(stages[-1])
    

def play(word):
    """
    Manages the game loop for guessing the word.
    """
    wrong_guesses = 0
    guessed_letters = set()
    
    word_completion=""
    for i in range(len(word)):
        if word[i] in guessed_letters or word[i]=='-':
            word_completion += word[i]
        else:
            word_completion += "_"

    print("Welcome to Hangman!")
    stages=display_hangman(wrong_guesses)
    while wrong_guesses < stages - 1 and word_completion != word:
        print(f"\nYou have {stages - wrong_guesses - 1} lives left.")
        print(f"Already guessed letters: {', '.join(guessed_letters)}")
        print(word_completion)

        guess = input("Guess a letter: ").upper()
        if guess in guessed_letters:
            print("You already guessed that letter!")
        elif guess in word:
            guessed_letters.add(guess)
            # Update word completion
            new_completion = ""
            for i in range(len(word)):
                if word[i] in guessed_letters:
                    new_completion += word[i]
                else:
                    new_completion += "_"
            word_completion = new_completion
        else:
            wrong_guesses += 1
            guessed_letters.add(guess)
            display_hangman(wrong_guesses)

    if word_completion == word:
        print(f"\nCongrats! You guessed the word {word} correctly.")
    else:
        print(f"\nYou ran out of lives. The word was {word}.")

# Main game loop
def main():
    word = get_word()
    play(word)

    while True:
        play_again = input("Play again? (yes/no): ").upper()
        if play_again != "YES":
            break
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
