# while loop
i = 0            # we assigned the value 0 to intialize it by 0.
while i <= 5 :   # if the condition is True then it enters the loop.
    print(i)
    i = i + 1   # we increase the value by 1.

# using while loop with user input
password = ""   # initializes the variable.
while password != "python@123":  # the loop runs as long the password in incorrect.
    password = input("Enter your password: ")

print("Access Granted!!")   # once the password matches it print the statement.


# while loop with if-else condition.
password = ""                                 # initializes the variable.
correct_password = "python@123"               # this variable stores your correct password.
while password != correct_password :           # the loop runs as long as the password is incorrect.
    password = input("Enter your password: ")
    if password == correct_password :          # if user enterscorrect password it will print "Access Granted!!"
        print("Access Granted!!")
    else:                                        # if user enters an incorrect password it will print "Try Again!" 
        print("Try Again!")
print("Good Job!")                       # prints "Good Job!" when the loop ends.

# counter-controlled loops
count = 1  # intializing value
while 5 >= count :
    print(count)
    count += 1  # increses count by +1 each time.

# sum 
total = 0
num = 1
while num <= 5 :
    total += num
    num += 1
print("Sum:",total)