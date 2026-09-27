import random

print("Hangman Game\n")
print("Guess a word letter by letter")

word_list = ["book", "table", "laptop", "phone", "game"]
secret_word = word_list[random.randint(0, len(word_list) - 1)]

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

while wrong_guesses < max_wrong:
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter
        else:
            display = display + "-"

    if "-" not in display:
        print("\nYou Guessed right")
        print("Your guess", display)
        print(f"Computer guessed: {secret_word}")
        break

    guess = input("\nEnter letter: ").lower()

    if guess in guessed_letters:
        print("\nYou already tried that letter")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        wrong_guesses = wrong_guesses + 1
        remaining = max_wrong - wrong_guesses
        print("\nInvalid Guess")
        print(f"Guesses remaining: {remaining}")

        if remaining == 0:
            print("\nGame Over")
            print(f"Correct word was: {secret_word}")
