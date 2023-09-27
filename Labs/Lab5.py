#Write a ‘guess the number game’ where a random number is generated and the user must guess the number. The program says if their number is too high or too low until the right answer is guessed.
import random

max_number = 100
secret_number = random.randint(1, max_number)

while True:
    guess = int(input(f"Enter your guess (1-{max_number}): "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break  # Exit the loop if the guess is correct
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
