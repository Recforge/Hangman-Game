# Let's create a hangman game
import time
import random

name = input("What is your name? ")
print("hello," + name, "let's play hangman!")
time.sleep(1)
print("game started...\n")
time.sleep(0.5)

# A list of hidden words
words = ['python', 'recforge', 'programming']
word = random.choice(words)

guesses = ""
turns = 5

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end=""),
            failed += 1
    if failed == 0:
        print("\n You won")
        break
    guess = input("\n guess the character: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\n Wrong")
        print("\n you left", + turns, "more guesses")
        if turns == 0:
            print("\n You loose")