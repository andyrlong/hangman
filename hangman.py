import random

# Create list of words
words = ['guitar', 'ukelele', 'bass', 'drums', 'violin']

# Chooses a random word from words
def pick_a_word():
    return random.choice(words)
print(pick_a_word())

# This function defines the winning and losing scenarios of the game
# If the guess is correct, the user wins. If the user runs out of lives, the lose.
def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print("You win!")
            break
        if lives_remaining == 0:
            print("You have been hung!")
            print("The word was " + word)
            break

# Prints the word with blanks and amount of lives that the user 
# has left, then allows the user to guess a letter or a whole word
def get_guess(word):
    print_word_with_blanks(word)
    print("Lives remaining: " + str(lives_remaining))
    guess = input("Guess a letter or whole word.")
    return guess

# Prints the word with blanks
def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word = display_word + letter
        else:
            display_word = display_word + '-'
    print(display_word)

# Processes whether the user guessed a letter or a word
def process_guess(guess, word):
    if len(guess) > 1:
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)

# If the guess is equal to the word, the user wins. 
# Otherwise, they lose a life. 
def whole_word_guess(guess, word):
    global lives_remaining 
    if guess == word:
        return True
    else:
        lives_remaining = lives_remaining - 1
        return False

# If the user guesses a letter incorrectly, the lose a life. 
def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True
    return False

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
        return True
    
# Main function
play()
            

