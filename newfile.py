import random

words = ["apple", "banana", "grape", "orange", "mango"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("Enter a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"Wrong! Attempts left: {attempts}")
    print(" ".join(guessed))

if "_" not in guessed:
    print("You guessed it!")
else:
    print("Out of attempts! Word was:", word)