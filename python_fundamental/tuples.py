## what is a tuple?
# --> tuple is collection of elements that can store multiple values, and different data types. It is ordered(maintains its position) and immutable(cannot change after creation).

# creatinng a tuple
student = ("raj", 18, "cse", 5.0)
print(student)

# tuples using indexing
fruits = ("mango", "apple", "cherry", "strawberry", "kiwi")
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

# tuples slicing
subjects = ("maths",10,"python",4.5)
print(subjects[1:4:2])
print(subjects[1:4])
print(subjects[:4])

# tuples are immutable
numbers = (60, 20, 30, 40, 50)
numbers[1] = 10
print(numbers)    # here you would get an type error cause tuple are immutable(meaning they cannot change after creation).
