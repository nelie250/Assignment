#TUYISHIME ERIC     223000313
#NTEZIRYAYO ELIE    223007446
#RUYANGA MERCI      223007985



#import random module
#import string module
import random
import string

# List of English words for selection
words = ["function","functioning","program","programing","programer","hangman","game"]

def get_word():
    # Randomly selects a word from the list
    return random.choice(words)

def display_word(word, guesses):
    # Displays the current word with guessed characters and dashes
    displayed_word = ""
    for letter in word:
        if letter.lower() in guesses:
            displayed_word += letter + " "
        else:
            displayed_word += "- "
    return displayed_word.strip()

def is_valid_guess(guess, warnings, guesses):
    # Checks if the guess is valid
    if len(guess) != 1 or guess not in string.ascii_letters:
        print("Invalid input! Please guess a single letter.")
        if warnings > 0:
            warnings -= 1
            print("You have", warnings, "warnings left.")
        else:
            print("You have no warnings left. You lose a guess!")
            return False
    elif guess.lower() in guesses:
        print("You've already guessed that letter!")
        if warnings > 0:
            warnings -= 1
            print("You have", warnings, "warnings left.")
        else:
            print("You have no warnings left. You lose a guess!")
            return False
    return True

def hangman():
    word = get_word()
    guesses = set()
    warnings = 3
    remaining_guesses = 6

    print("The word contains", len(word), "letters.")

    while True:
        print("You have", remaining_guesses, "guesses remaining.")
        print("Letters not yet used:", " ".join(sorted(list(set(string.ascii_lowercase) - guesses))))

        if remaining_guesses <= 0:
            print("You lost! The word was:", word)
            break

        if set(word.lower()) == guesses:
            score = remaining_guesses * len(set(word))
            print("Congratulations, you won!")
            print("Your score is:", score ,"/", len(set(word))*6)
            break

        guess = input("Please guess a letter: ").lower()

        if not is_valid_guess(guess, warnings, guesses):
            if guess in "aeiou":
                remaining_guesses -= 2
            else:
                remaining_guesses -= 1
            continue

        guesses.add(guess)
        if guess in word.lower():
            print("Good guess!")
        elif guess in "aeiou":
            print(" That's a vowel not in the word.")
            remaining_guesses -= 2
        else:
            print(" letter is not in the word.")
            remaining_guesses -= 1

        print("Word:", display_word(word, guesses))
        print()

# Start the game
hangman()