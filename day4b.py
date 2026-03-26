import random

def play_game():
    secret_number = random.randint(1, 10)
    tries = 0
    max_tries = 5

    print("\nWelcome to the Number Guessing Game!")
    print("You have 5 tries to guess a number between 1 and 10!")

    while tries < max_tries:
        guess = int(input("Take a guess: "))
        tries = tries + 1

        if guess < secret_number:
            print("Too low! " + str(max_tries - tries) + " tries left!")
        elif guess > secret_number:
            print("Too high! " + str(max_tries - tries) + " tries left!")
        else:
            print("YOU GOT IT in " + str(tries) + " tries! 🎉")
            return

    print("Game over! The number was " + str(secret_number))

while True:
    play_game()
    again = input("\nPlay again? (yes/no): ")
    if again != "yes":
        print("Thanks for playing Sparkle! 👋")
        break