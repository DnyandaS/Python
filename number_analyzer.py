# Project: Number Analyzer
# Purpose: Analyze a number entered by the user.
# Concepts: Variables, conditions, loops and arithmetic operators.

number = int(input("Enter a Number: "))
print("You Entered: ", number)

# check whether a number is odd or even.
if number % 2 == 0  :
    print("The number is even")
else:
    print("The number is odd")

#check whether a number is positive, negative or zero.
if number == 0 :
    print("The number is Zero")
elif number > 0 :
    print("The number is Positive")
else: 
    print("The number is Negative")

#number of digits present
digits = len(str(abs(number)))      #abs returns the absolute value of a number. Then we converted it to a string and then found the length of that string.
print("The number of digits are: ", digits)

#sum of numbers using a while loop
sum_of_digits = 0
absolute_num = abs(number)
while absolute_num > 0 :
    last_digit = absolute_num % 10       # % 10 extracts the last digit of the number.
    absolute_num = absolute_num // 10    # // 10 removes the last digit of the number.
    sum_of_digits = sum_of_digits + last_digit
print("The sum of digits are: ", sum_of_digits)

# reversing a number using while loop
reversed_num = 0
absolute_num = abs(number)
while absolute_num > 0 :
    last_digit = absolute_num % 10
    absolute_num = absolute_num // 10
    reversed_num = reversed_num * 10 + last_digit       # *10 shifts the digits to the left and adds the last digit to the reversed number.
print("The reversed number is: ", reversed_num)