import random

# Set the range
low = 1
high = 50

# Generate a random number within the range
correct_answer = random.randrange(low, high + 1)

# Allow the user 5 chances to guess the correct number
for attempt in range(5):
    # Ask the user for input
    user_guess = int(input(f"Guess the number between {low} and {high}: "))

    # Check if the user's guess is correct
    if user_guess == correct_answer:
        print("You Win!")
        break
    elif user_guess < correct_answer:
        print("Correct answer is greater!")
    else:
        print("Correct answer is smaller!")

# If the loop completes without a correct guess
else:
    print(f"You lose! The correct answer was {correct_answer}.")
