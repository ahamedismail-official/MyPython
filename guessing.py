import random


def generate_random_number():
    return random.randint(1, 100)


def is_even(number):
    return number % 2 == 0


def play_game():
    score = 0
    total_rounds = int(input("Enter the number of rounds you want to play: "))

    for _ in range(total_rounds):
        random_number = generate_random_number()
        print("A random number has been generated between 1 and 100.")

        guess = int(input("Player 2, guess the number: "))

        if guess == random_number:
            print("Congratulations! You guessed the number right on the first try!")
            score += 100
        else:
            choice = input("Wrong guess! Do you want a clue? (yes/no): ").lower()
            if choice == "yes":
                if is_even(random_number):
                    print("The number is even.")
                else:
                    print("The number is odd.")

                guess = int(input("Player 2, guess the number again: "))

                if guess == random_number:
                    print("Congratulations! You guessed the number right with a clue!")
                    score += 50
                else:
                    print(f"Sorry, the correct number was {random_number}. You lose 50 points.")
                    score -= 50
            else:
                print(f"Sorry, the correct number was {random_number}. You lose 100 points.")
                score -= 100

        print(f"Your current score is: {score}")

        if input("Press 'q' to quit or any other key to continue: ").lower() == "q":
            break

    print("Game Over!")
    print(f"Your final score is: {score}")


play_game()
