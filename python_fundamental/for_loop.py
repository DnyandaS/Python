## for loop
print("simple loop")
for i in range(5):
    print(i)  # this will print range (0 to 4).

# range(start, stop)
print("range(start, stop)")
for i in range(1,6):
    print(i)  # this will print range (1 to 5).

# range (start, stop, step)
print("range (start, stop, step)")
for i in range(0,9,2):      # step is used to incrment the loop by that number.
    print(i)   # this will print range (0,2,4,6,8).

# counting backwards
print("counting backwards")
for i in range(6,0,-1):   #range(starting number, stopping point(excluded), iteration )
    print(i)

# for loop with conditions
print("if-condition")
for i in range(1,31,5):
    if i % 2 == 0 :
        print(i)
    else:
        print("Try again")