## for loop
print("simple loop --->")
for i in range(5):
    print(i)  # this will print range (0 to 4). Since we have not given any number to start with it will start with zero "0" .

# range(start, stop)
print("range(start, stop) --->")
for i in range(1,6):
    print(i)  # this will print range (1 to 5).

# range (start, stop, step)
print("range (start, stop, step) --->")
for i in range(0,9,2):      # step is used to incrment the loop by that number.
    print(i)   # this will print range (0,2,4,6,8).

# counting backwards
print("counting backwards --->")
for i in range(6,0,-1):   #range(starting number, stopping point(excluded), iteration )
    print(i)

# for loop with conditions
# if condition
print("if condition --->")
for i in range(1,9):
    if i % 2 == 0 :
        print(i)

# if-else condition
print("if-else condition --->")
for i in range(15):
    if i % 5 == 0 :
        print("it is divisible")
    else:
        print("not divisible")

# if-elif-else condition
print("if-elif-else condition --->")
n = int(input("input a number to check wether a number is positive, negative, odd or even: "))
for i in range(n,n+1):  # n+1 to include n, cause range() excludes the stop value.
    if (i > 0) and (i % 2 == 0):
        print("The number is positive and even")
    elif (i < 0) and (i % 2 == 0):
        print("The number is negative and even")
    elif (i < 0)and (i % 2 != 0):
        print("The number is negative and odd")
    elif (i > 0) and (i % 2 != 0):
        print("The number is positive and odd")
    else:
        print("The number is zero")
