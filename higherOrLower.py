import random

# secret number variable can be changed based on what the programmer desires
secret_number = random.randint(1, 501)

# guess counter keeps track of the number of guesses

guess_counter = 0

# guess limit is the amount of guesses the user is allowed to make
guess_limit = 9

# counter variable inside the while loop and to display afterwards
amount_of_guesses = 0

# number to compare to secret number inside the while loop
guess = 0

# boolean variable to check if player has won or lost
b = False

print("You have 10 guesses to guess the secret number. Choose wisely.")
print("I will tell you if you are higher or lower as you go.")
print("The number is between 0 to 500.")
print()
while guess_counter < guess_limit and guess != secret_number:
    guess = input("Enter your guess: ")
    amount_of_guesses += 1
    guess_counter += 1
    if int(guess) == secret_number:
        b = True
        break
    elif int(guess) < secret_number:
        print("Higher!")
    elif int(guess) > secret_number:
        print("Lower!")


if (b):
    print()
    print(f"You won!")
    print(f"You took {amount_of_guesses} guess(es) to reach the secret number of {secret_number}")
else:
    print()
    print(f"You lost. You did not reach the secret number.")
