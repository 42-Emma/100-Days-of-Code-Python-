import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
# print(chosen_word)

chosen_word_list = []
for x in range(len(chosen_word)):
    chosen_word_list += '_'
# print(chosen_word_list)

game_on = True

while game_on:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word_list:
        print(f"You've already guessed {guess}")

    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            chosen_word_list[letter] = guess
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose")
            game_on = False
    # print (chosen_word_list)

    display = ''.join(chosen_word_list)
    print(display)

    if display == chosen_word:
        game_on = False
        print("You win")
    
    print(stages[lives])

