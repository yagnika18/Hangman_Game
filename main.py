import random

# Hangman stages (from full lives to 0)
stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',  # 6 lives left
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',  # 5 lives left
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',  # 4 lives left
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',  # 3 lives left
    '''
      +---+
      |   |
      O   |
     /|\  |
      |   |
          |
    =========
    ''',  # 2 lives left
    '''
      +---+
      |   |
      O   |
     /|\  |
     /|   |
          |
    =========
    ''',  # 1 life left
    '''
      +---+
      |   |
      O   |
     /|\  |
     /|\ |
          |
    =========
    '''   # 0 lives left - Game Over
]

# Word list
word_list = ['python', 'hangman', 'developer', 'challenge', 'program']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game setup
display = ['_'] * word_length
lives = 6
guessed_letters = []

print("🎮 Welcome to Hangman with Stages!")
print(" ".join(display))

# Game loop
while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print(f"🔁 You already guessed '{guess}'")
        continue
    else:
        guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Good guess!")
    else:
        lives -= 1
        print(f"❌ Wrong! Lives left: {lives}")
        print(stages[6 - lives])

    print("Word:", " ".join(display))
    print("Guessed Letters:", guessed_letters)

# Final result
if '_' not in display:
    print("🎉 Congratulations! You won!")
else:
    print("💀 Game Over. You lost.")
    print("The word was:", chosen_word)
