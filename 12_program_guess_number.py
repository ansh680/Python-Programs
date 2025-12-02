import random

number = random.randint(1, 9)
guess = int(input("Guess the number (1–9): "))

if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")
else:
    print("Correct! You guessed it right.")
