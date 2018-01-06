#!/usr/bin/env python

operation = input("""Please type in the math operation you would like to complete :
 + for Addition 
 - for Subtrastion
 * for Multiplication
 / for Division """)

number_1 = int(input("Enter your first number:  "))
number_2 = int(input("Enter your second number:  "))

if operation == '+':
    print('{} + {} = ' .format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{}  - {} = '.format(number_1,number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} ='.format(number_1,number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1,number_2))
    print(number_1 / number_2)

else:
    print('you habe not typed a valid operator, please run the program again.')