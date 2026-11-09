# while loop
i = 0            # we assigned the value 0 to intialize it by 0.
while i <= 5 :   # if the condition is True then it enters the loop.
    print(i)
    i = i + 1   # we increase the value by 1.

# using while loop with user input
password = ""   # initializes the variable.
while password != "python@123":  # the loop runs as long the password in incorrect.
    password = input("Enter password: ")

print("Access granted!")   # once the password matches it print the statement.
