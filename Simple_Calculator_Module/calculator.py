# PRO1002 Work Requirement 02
# Task 8. Simple Calculator Module

# Part 1: Create a module called calculator.py that has functions for add, subtract, multiply, and divide.

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    # ...if the user chooses division by zero, handle the ZeroDivisionError and print an error message.
    if b == 0:
        raise ZeroDivisionError('division_by_zero')
    
    return a / b