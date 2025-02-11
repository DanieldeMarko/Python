#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniel.Karapandov
#
# Created:     04/08/2022
# Copyright:   (c) Daniel.Karapandov 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()



# Store input numbers:
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
num3 = input('Enther third number')
# Add two numbers
sum = float(num1) + float(num2) + float(num3)
# Subtract two numbers
min = float(num1) - float(num2) - float(num3)
# Multiply two numbers
mul = float(num1) * float(num2) * float(num3)
#Divide two numbers
div = float(num1) / float(num2) / float(num3)
# Display the sum
print('The sum of {0}, {1} and {2} is {3}'.format(num1, num2, num3, sum))

# Display the subtraction
print('The subtraction of {0}, {1} and {2} is {3}'.format(num1, num2, num3, min))
# Display the multiplication
print('The multiplication of {0}, {1} and {2} is {3}'.format(num1, num2, num3, mul))
# Display the division
print('The division of {0}, {1}, {2} is {3}'.format(num1, num2, num3, div))