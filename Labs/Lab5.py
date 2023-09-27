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