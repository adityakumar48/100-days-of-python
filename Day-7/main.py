from hangman_words import word_list
import random
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
wordLength = len(chosen_word)
display = []
end_of_game = False


# Display blanks

for _ in range(wordLength):
    display += "_"
print(display)


lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(wordLength):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
