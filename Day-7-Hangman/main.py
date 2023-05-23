from replit import clear
import random
from hangman_words import word_list
from hangman_art import stages, logo


print(logo)
chosen_word = random.choice(word_list)
# print(f"DEBUG: The chosen_word is: {chosen_word}.")
display = []
word_length = len(chosen_word)
lives = 6 # number of stages the hangman has
print(stages[6])

for _ in range(word_length):
    display += "_"
print(' '.join(display))

end_of_game = False

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed `{guess}`.")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed `{guess}`. That's not in the word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose!")

    print(stages[lives])
    print(f"{' '.join(display)}")

    if '_' not in display:
        end_of_game = True
        print("\nYou win!")
