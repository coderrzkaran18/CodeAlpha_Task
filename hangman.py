import random

# Step 1: Predefined list of words
words = ["python", "hangman", "college", "analytics", "project"]

# Step 2: Randomly choose a word
word = random.choice(words)
word_letters = list(word)  # convert word into list of characters
guessed_letters = ["_"] * len(word)  # underscores for hidden letters

# Step 3: Set maximum incorrect guesses
max_attempts = 6
attempts = 0

print("🎮 Welcome to Hangman!")
print("Guess the word: ", " ".join(guessed_letters))

# Step 4: Game loop
while attempts < max_attempts and "_" in guessed_letters:
    guess = input("Enter a letter: ").lower()

    if guess in word_letters:
        # Reveal all positions of the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed_letters[i] = guess
        print("✅ Correct guess!")
    else:
        attempts += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - attempts}")

    print("Word: ", " ".join(guessed_letters))

# Step 5: End game result
if "_" not in guessed_letters:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)