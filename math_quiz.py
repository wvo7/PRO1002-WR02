# PRO1002 Work Requirement 02
# Task 4: Math Quiz with Exception Handling

# Use the random module (from the standard library) to generate two random integers and ask the user to add them.
# Try to convert the user's input to an integer. If that fails (e.g., user enters non-digit input), handle the exception and print "Invalid input!".
# If the input is valid, check if the answer is correct and print a message accordingly.


# Import module

import random

# Generate numbers

nr1 = random.randint(1,13)
nr2 = random.randint(1,13)

correct_answer = nr1 + nr2

# Introducing our quiz master

print("Hello! I'm Ellie, and I'll be your math quiz master for today!")

# Give user 3 chances to get the answer right / provide valid number.

for attempt in range(1,4):
    # User prompt
    user_input = input(f"What's {nr1} + {nr2}?\n")

    # Exception handling

    try:
        # Attempting to convert user input from string to integer.
        user_guess = int(user_input)

        # Check if the user's answer is correct
        if user_guess == correct_answer:
            print("You got it!\nDon't be to smug; it's basic math.")
            break # Escape the loop
        else:
            print(f'Wrong. You have {3 - attempt} attempts left. Try again!')

    except ValueError:
        # Only runs if the user doesn't type a number
        print('We only accept whole number in this math quiz. Try again.')

else:
    print(f'The answer was {correct_answer}.')
    print("You're either not taking this seriously, or exceptionally bad at math.\nEither way; I quit.")