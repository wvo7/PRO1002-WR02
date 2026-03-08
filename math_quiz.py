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

# User prompt

user_input = input(f"What's {nr1} + {nr2}?\n")

# Exception handling

try:
    # Attempting to convert user input from string to integer.
    user_guess = int(user_input)

    # Check if the user's answer is correct
    if user_guess == correct_answer:
        print('You got it!')
    else:
        print(f'The number we were looking for was {correct_answer}. Better luck next time!')

except ValueError:
    # Only runs if the user doesn't type a number
    print('We only accept whole number in this math quiz. Try again.')