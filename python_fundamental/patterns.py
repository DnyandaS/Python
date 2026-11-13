## patterns using for loop.
# pattern 1 : square
print("square-->")
n = 5
for i in range(1,n+1):
    print("* " * n)


# pattern 2 : right triangle
print("right triangle-->")
n = 5
for i in range(1,n+1):
    print("* " * i)

# pattern 3 : inverted triangle
print("inverted triangle-->")
n = 5
for i in range(n,0,-1):
    print("* " * i)

# pattern 4 : reverse triangle
print("reverse triangle-->")
n = 5
for i in range(n):
    print("  " * i, end = "")
    for j in range(n-i):
        print("*", end = " ")
    print()

# pattern 5 : increasing numbers
print("increasing numbers-->")
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end = " ")
    print()

# pattern 6 : repeated numbers
print("repeated numbers-->")
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end = " ")
    print()

# pattern 7 : pyramid
print("pyramid-->")
n = 5
for i in range(1,n+1):
    print("  " * (n-i), end=" ")
    for j in range(2*i-1):
        print("* ",end = "")
    print()

# pattern 8 : hollow square
print("hollow square-->")
n = 5
for i in range(1,n+1):                                      # i represents the row, and j represents the column.
    for j in range(1,n+1):
        if i == 1 or i == n or j == 1 or j == n :
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

# pattern 9 : concentric square patterns
print("concentric square pattern-->")
n = 5
size = 2*n-1
for i in range(size):
    for j in range(size):
        minimum = min(i,j,(size-1-i), (size-1-j))   # min(top,left,bottom,right)
        value = n - minimum
        print(value, end = "  ")
    print()

# pattern 10 : butterfly
print("butterfly-->")
n = 5
## upper half
for upper in range(1,n+1):
    # upper left wing
    for upperleft in range(upper):
        print("*", end = " ")
    # upper middle space
    for upperspace in range(2*(n-upper)):
        print(" ", end = " ")
    # upper right wing
    for upperright in range(upper):
        print("*", end = " ")
    print()
## lower half
for lower in range(n-1,0,-1):
    # lower left wing
    for lowerleft in range(lower):
        print("*",end = " ")
    # middle spaces
    for lowerspace in range(2*(n-lower)):
        print(" ", end = " ")
    # lower right wing
    for lowerright in range(lower):
        print("*" , end = " ")
    print()


# pattern 11 : diamond
print("diamond-->")
n = 5
# upper half
for i in range(1,n+1):
    print("  " * (n-i), end = " ")
    for j in range(1,2*i):
        print("*",end = " ")
    print()
# lower half
for i in range(n-1,0,-1):
    print("  " * (n-i), end = " ")
    for j in range(1,2*i):
        print("*",end = " ")
    print()

# pattern 12 : hollow pyramid
print("hollow pyramid-->")
n = 5
for i in range(1,n+1):
    print("  " * (n-i),end = "")
    for j in range(1,2*i):
        if i == n or j == 2*i-1 or j == 1 :
            print("*", end = " ")
        else:
            print(" " , end = " ")
    print()

# pattern 13 : floyd's triangle
print("floyd's triangle-->")
n = 5
counter = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(counter, end = " ")
        counter = counter + 1
    print()