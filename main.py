import random
import hangman_art
import hangman_wordlist
import os




def check_guess():
    letter_found = False
    for _ in range(len(target_word)):
        if target_word[_] == guess:
            display[_] = guess
            letter_found = True
    return letter_found


lives = 6


target_word = random.choice(hangman_wordlist.word_list)
display = []

for letter in target_word:
    display.append("_")

print(hangman_art.logo)
# print(target_word)
print(" ".join(display))

end_of_game = False
guessed_letters = []
while not end_of_game:
    guess = input("Guess a letter:  ").lower()
    os.system('cls')
    if guess in guessed_letters:
        print(f"You have already guessed '{guess}' make another selection.")
        continue
    else:
        guessed_letters.append(guess)

    if not check_guess():
        lives -= 1
        print(f"Your guess of: {guess} is incorrect. You have {lives} guesses remaining.")

    print(" ".join(display))
    print(hangman_art.stages[lives])

    if "_" not in display:
        end_of_game = True

        print("You win!")
    if lives == 0:
        end_of_game = True
        print(f"You lose.  The word was '{target_word}'")

