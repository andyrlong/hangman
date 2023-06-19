import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' or ' ' in words:
        word = random.choice(words)
    return word

def hangman():
    # Word chosen
    word = get_valid_word(words)
    # Letters in a word
    word_letters = set(word)
    alphabet = (string.ascii_uppercase)
    # Letters that have been used
    used_letters = set()

    lives = 7

    while len(word_letters) > 0 and lives > 0:

        print("You have used the following letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print("Current word: ", " ".join(word_list))

        # Letter guessed by the user
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter not found in word.")
        elif user_letter in used_letters:
                    print("You have already guessed that letter.")
        else:
                    print("Invalid input.")

    if lives == 0:
          print(lives_visual_dict[lives])
          print(f"You died. The word was {word}")
    else:
          print("You guessed the word!")

if __name__ == '__main__':
    hangman()

            

