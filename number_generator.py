# Project: Number Generator
# Purpose: Generate number sequences, multiplication tables,and perform basic numerical operations.
# Concepts: Variables, input, type conversion, loops, range(), conditional statements and arithmetic operators.

# number sequence
print("\nNumber Sequence Generator")
number = int(input("Enter a number to generate sequence: "))
for i in range(1, number + 1):  #took range from 1 to number + 1 to generate sequence from 1 to the entered number.
    print(i, end=" ")

# reverse number sequence
print("\nReverse Number Sequence Generator")

for i in range(number , 0 , -1):   #took range from number to 0 with step -1 to generate reverse sequence.
    print(i, end = " ")

# multiplication table
print("\nMultiplication Table Generator")

for i in range(1,11):              #took range from 1 to 10 to generate multiplication table.
    print(number,"X", i , "=", number * i)

# sum of numbers
print("\nSum of Numbers Generator")

total= 0                        #took a variable total to store the sum of numbers from 1 to the entered number.
for i in range(1, number + 1):  #took range from 1 to number + 1 to calculate the sum of numbers from 1 to the entered number.
    total += i
print("The sum of numbers from 1 to", number, "is:", total)

#even or odd number generator
print("\nEven or Odd Number Generator")

for i in range(1, number + 1):         #took range from 1 to number + 1 to check if the numbers from 1 to the entered number are even or odd.
    if i % 2 == 0:                   
        print(i, "is even")
    else:
        print(i, "is odd")
    
