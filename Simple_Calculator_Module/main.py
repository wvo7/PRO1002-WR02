# PRO1002 Work Requirement 02
# Task 8. Simple Calculator Module

# Part 2: In your main script, import calculator.

import calculator

# Ask the user for two numbers and an operation.

def run_calculator():
    try:
        # User input.
        nr1 = float(input('Enter first number: '))
        nr2 = float(input('Enter second number: '))
        operation = input('Choose operation: ')

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
            print("Invalid operation. Use +, -, *, or /.")
            return
        
        # Print the result of the calculation.
        print(f'The result is: {result}.')

    except ValueError:
        print('Error. Enter a valid number.')
    except ZeroDivisionError as zero_error:
        print(f'Error: {zero_error}')

run_calculator()