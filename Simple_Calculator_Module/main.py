# PRO1002 Work Requirement 02
# Task 8. Simple Calculator Module

# Part 2: In your main script, import calculator.

import calculator

# Introduce our Calculator persona

print("Hello! I'm Ellie, and I'll be your calculatoring assistant today!\nLet's do some math!")

# Ask the user for two numbers and an operation.

def run_calculator():
    try:
        # User input.
        input_str1 = input('Enter your first number: ')
        input_str2 = input('Enter your second number: ')
        operation = input('And choose operation: ')

        # Convert to float.
        nr1 = float(input_str1)
        nr2 = float(input_str2)

        # Checking if inputs are single digits (Ellie doesn't like that)
        if 0 <= nr1 <= 9 and 0 <= nr2 <= 9 and operation !='/':
            print('Do you really need my help with single-digit math, or are you just insulting my intelligence?')
            print("I'm not gonna entertain this nonsense.")
            return

        # Perform the operation, and if the user chooses division by zero, handle the ZeroDivisionError and print an error message.
        if operation == '+':
            result = calculator.add(nr1,nr2)
        elif operation == '-':
            result = calculator.subtract(nr1,nr2)
        elif operation == '*':
            result = calculator.multiply(nr1,nr2)
        elif operation == '/':
            result = calculator.divide(nr1,nr2)
        else:
            print("Don't you know what an operation is?\nI'll help you out: +, -, *, or /.")
            return
        
        # Print the result of the calculation.
        print(f'The result is: {result}. Yay math!')

    except ValueError:
        print("404. That's no number of mine.")
    except ZeroDivisionError:
        print(f'Dividing 0 by 0 is a crime around here.\nAre you trying to crash me?? Get outta here.')

run_calculator()