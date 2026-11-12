## break
# break statement using for loop
print("break statement using for loop")
for i in range(1,11):
    if i == 5 :
        break
    print(i)  # it will break the loop when the condition is satisfied

# break statement using while loop
print("break statement using while loop")
n = 1
while n < 10:
    if n == 5 :
        break 
    print(n)
    n += 1

## continue
# continue statement using for loop
print("continue statement using for loop")
for i in range(1,11):
    if i == 5 :
        continue  # this will print all numbers except "5"
    print(i)

# continue statement using while loop
print("continue statement using while loop")
n = 0
while n < 11:
    n += 1
    if n == 5 :
        continue
    print(n)

## pass
# pass statement using for loop
print("pass statement using for loop")
for i in range(1,6):
    if i == 5 :
        pass    # pass does nothing. It allows you to leave a loop or conditional block empty without causing a syntax error.
    print(i)

# pass statement using while loop
print("pass statement using while loop")
n = 0
while n < 6 :
    n += 1
    if n == 5 :
        pass
    print(n)