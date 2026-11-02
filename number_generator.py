# Project: Number Generator
# Purpose: Generate number sequences, multiplication tables,and perform basic numerical operations.
# Concepts: Variables, input, type conversion, loops, range(), conditional statements and arithmetic operators.

# number sequence
number = int(input("Enter a number to generate sequence: "))
for i in range(1, number + 1):
    print(i, end=" ")

# reverse number sequence
number = int(input("Enter a number to generate reverse sequence: "))
for i in range(number , 0 , -1):
    print(i, end = " ")

# multiplication table
number = int(input("Enter a number to generate a multiplication table: "))
for i in range(1,11):
    print(number,"X", i , "=", number * i)

# sum of numbers
number = int(input("Enter  a number to calculate it's sum: "))
total= 0
for i in range(1, number + 1):
    total += i
print("The sum of numbers from 1 to", number, "is:", total)

# even or odd number generator
number = int(input("Enter a number to check if it's even or odd: "))
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
    
