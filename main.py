
import random
import hangman_art
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(f"{hangman_art.logo}")
display = []
for _ in range(word_length):
    display += "_"
print(display)
guesscheck = []
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  if guess not in guesscheck:
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
    guesscheck += guess
    if guess not in chosen_word:
      lives -= 1
      print(f"You loose a life. Lives left: {lives}\n{hangman_art.stages[lives]}")
      if lives == 0:
        end_of_game = True
        print("You lose.")
        print(f"The word is {chosen_word}")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
  else:
    print(f"You already guessed the letter {guess}, try again")
