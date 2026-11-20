## list methods

# 1. append()
list_a = []
for i in range(1,4):
    list_a.append(i)   # adds an element to the en of the list
print(list_a)

# 2. extend()
# list_a = ["apple","banana"]
list_a = [1,2,3]
list_b = [4,5,6]
list_a.extend(list_b)    # add elements to the end of the list
print(list_a)

# 3. insret()
list_a = [1,2,4,5]
list_a.insert(2,3)   # insert(index, the no. you wanna add)
print(list_a)

# 4. pop()
list_a = [1,2,3]
list_a.pop()    # removes last element
print(list_a)

# 5. remove()
list_a = [1,2,3,4,3]
list_a.remove(3)   # removes the first matching element from the list
print(list_a)

# 6. clear()
list_a = [1,2,3,4]
list_a.clear()
print(list_a)   # removes all items

# 7. index()
list_a = [1,2,3,4]
list_a.index(3)
print(list_a)

# 8. count()
list_a = [1,2,2,3,2,4,5,2,6]
list_a.count(2)
print(list_a)

# 9. sort()
list_a = [1,3,2,4,5,6]
list_a.sort()    # sorts the list
print(list_a)

# sort and sorted
# sort modiefies the list and sorted creates a new list
list_a = [1,3,2,4]
sorted(list_a)
print(list_a)

