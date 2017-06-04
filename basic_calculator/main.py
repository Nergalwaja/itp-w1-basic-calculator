"""This is the entry point of the program."""
"""This is a basic python program that takes input, passes it to the calculator function, and outputs a calculation specified by the user: IE. + - * / """

def basic_calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    else:
        return 'Invalid operation'


basic_calculator(1, 7, 'add')
basic_calculator(5, 2, 'subtract')
basic_calculator(3, 4, 'multiply')
basic_calculator(12, 3, 'divide')
basic_calculator(3, 4, 'what')
