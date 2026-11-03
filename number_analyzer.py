# Project: Number Analyzer
# Purpose: Analyze a number entered by the user.
# Concepts: Variables, conditions, loops and arithmetic operators.

number = int(input("Enter a Number: "))
print("\nYou Entered: ", number)

# check whether a number is odd or even.
print("\nOdd or Even Number Analyzer")
if number % 2 == 0  :
    print("\nThe number is even")
else:
    print("\nThe number is odd")

#check whether a number is positive, negative or zero.
print("\nPositive, Negative or Zero Number Analyzer")
if number == 0 :
    print("\nThe number is Zero")
elif number > 0 :
    print("\nThe number is Positive")
else: 
    print("\nThe number is Negative")

#number of digits present
digits = len(str(abs(number)))      #abs returns the absolute value of a number. Then we converted it to a string and then found the length of that string.
print("\nThe number of digits are: ", digits)

#sum of numbers using a while loop
sum_of_digits = 0
absolute_num = abs(number)
while absolute_num > 0 :
    last_digit = absolute_num % 10       # % 10 extracts the last digit of the number.
    absolute_num = absolute_num // 10    # // 10 removes the last digit of the number.
    sum_of_digits = sum_of_digits + last_digit
print("\nThe sum of digits are: ", sum_of_digits)

# reversing a number using while loop
reversed_num = 0
absolute_num = abs(number)
while absolute_num > 0 :
    last_digit = absolute_num % 10
    absolute_num = absolute_num // 10
    reversed_num = reversed_num * 10 + last_digit       # *10 shifts the digits to the left and adds the last digit to the reversed number.
print("\nThe reversed number is: ", reversed_num)