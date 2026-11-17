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
# numbers[1] = 10
# print(numbers)    # here you would get an type error cause tuple are immutable(meaning they cannot change after creation).

# converting string to tuple
colour = "blue"
print(tuple(colour))

#converting list to tuple
number_list = [1, 2, 3, 4, 5]
print(tuple(number_list))

# converting sequence to tuple
sequence = range(5)
sequence_a = range(1,6)
print(tuple(sequence))
print(tuple(sequence_a))


# tuples membership check

## in 
number = (1,2,3,4,5,6,7,8,9,0)
check = 5 in number
print(check)
print(18 in number)

## not in
re_check = 15 not in number
print(re_check)
print(2 not in number)

# list membership check
num = [10,20,30,40,50]
print(10 in num)
print(10 not in num)

# string membership check
word = "apple"
print("le" in word)
print("ap" not in word)