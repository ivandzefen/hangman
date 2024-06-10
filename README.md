# hangman
hangman game
## Hangman Game 

This is a Python implementation of the classic Hangman game! Test your vocabulary and guess the hidden word letter by letter.

### How to Play

1. **Run the Script:**
   Save the code as a Python file (`hangman.py`) and run it from your terminal using:

   ```bash
   python hangman.py
   ```

2. **Gameplay:**
   The game will welcome you and choose a random word from a list. You'll see an empty word with underscores representing each letter and the hangman illustration (starting with a full body).

3. **Guessing Letters:**
   In each turn, guess a letter by entering it (uppercase or lowercase) and pressing enter.
   * If the letter is in the word, it will be revealed in its corresponding positions.
   * If the letter is not in the word, a body part is added to the hangman illustration, and you lose a life.

4. **Winning or Losing:**
   The game continues until you either:
     * Guess all the letters correctly and reveal the entire word (you win!)
     * Run out of lives by guessing wrong letters too many times (the hangman is complete, and the word is revealed - you lose!)

5. **Playing Again:**
   After each round, the game will ask if you want to play again. Enter "YES" to start a new game with a new word, or anything else to quit.

### Requirements

This script requires Python to be installed on your system. You can download and install Python from the official website [https://www.python.org/downloads/](https://www.python.org/downloads/).


### Additional Notes

* The game reads words from a text file named `words.txt`. Make sure this file is in the same directory as the Python script. You can add your own words to this file, each on a separate line.

I hope you enjoy this Hangman game!
