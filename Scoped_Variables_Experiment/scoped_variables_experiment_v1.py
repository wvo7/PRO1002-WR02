# PRO1002 Work Requirement 02
# Task 7: Scoped Variables Experiment

# 1. Write a function that defines a variable inside it, and print it.

def outer_function():
    test_variable = 'Local function'
    print(f'Calling the function: {test_variable}')

outer_function()

# 2. Outside the function, define a variable with the same name and a different value, and print it.

test_variable = 'Global function'

print(f'Print from global scope: {test_variable}')

# 3. Call the function and print again to show scope differences.

# Proving the Global variable wasn't affected by the Local variable.
print(f'Comparison:')
outer_function()
print(f'Still outside: {test_variable}')

# 4. Add another nested function or loop to show how scope changes in that context as well.

def scope_demo():
    inner_variable = 'Initial value'
    print(f'Inside loop: {inner_variable}')

    # Loops share the function's scope and are 'transparent.'
    for i in range(1):
        inner_variable = 'Changed by loop'
        print(f'Inside loop: {inner_variable}')

    # Creates isolated layer of scope.
    def nested_function():
        inner_variable = 'New nested version'
        print(f'Inside nest: {inner_variable}')

    nested_function()

    # Confirms the nested_function's change was temporary.
    print(f'Back in function, inner_variable is still: {inner_variable}')

scope_demo()