# # while loop
# i = 0            # we assigned the value 0 to intialize it by 0.
# while i <= 5 :   # if the condition is True then it enters the loop.
#     print(i)
#     i = i + 1   # we increase the value by 1.

# # using while loop with user input
# password = ""   # initializes the variable.
# while password != "python@123":  # the loop runs as long the password in incorrect.
#     password = input("Enter your password: ")

# print("Access Granted!!")   # once the password matches it print the statement.


# # while loop with if-else condition.
# password = ""                                 # initializes the variable.
# correct_password = "python@123"               # this variable stores your correct password.
# while password != correct_password :           # the loop runs as long as the password is incorrect.
#     password = input("Enter your password: ")
#     if password == correct_password :          # if user enterscorrect password it will print "Access Granted!!"
#         print("Access Granted!!")
#     else:                                        # if user enters an incorrect password it will print "Try Again!" 
#         print("Try Again!")
# print("Good Job!")                       # prints "Good Job!" when the loop ends.

# # counter-controlled loops
# count = 1  # intializing value
# while 5 >= count :
#     print(count)
#     count += 1  # increses count by +1 each time.

# # sum 
# total = 0   # starts the sum at 0
# num = 1   # starts counting from 1
# while num <= 5 :   # condition
#     total += num  # adds the current num to total
#     num += 1     # increments
# print("Sum:", total)  # prints the sum


# print multiplication table by loop
number = int(input("Enter a number: "))
i = 1
while i <= 10 :
    print(number, "X", i, "=", number * i)
    i += 1
print("Well done!!")


# printing patterns using while loops

## pattern 1: square
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
i = 1 
while i <= rows :  # controls rows (outer loop)
    j = 1
    while j <= columns :    # controls columns (inner loop)
        print("*", end = " ")   # prints "*" on same line
        j += 1
    i += 1
    print()    # moves to next line after each row

## pattern 2: right angled triangle
rows = int(input("Enter number of rows: "))
i = 1
while i <= rows :
    j = 1
    while j <= i :
        print("*", end = " ")
        j += 1
    i += 1
    print()