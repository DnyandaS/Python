# Topic: Python Lists
# Purpose: Create a program to store, analyze, and manage students' marks using lists.
# Concepts: Lists, indexing, list methods (sum(), reverse(), sort(), reverse()), len(), and basic arithmetic.
 
# Student marks analyzer
python = int(input("Enter marks for python out of hundred: "))
maths = int(input("Enter your marks for maths out of hundred: "))
english = int(input("Enter your marks for english out of hundred: "))
physics = int(input("Enter your marks for physics out of hundred: "))
chemistry = int(input("Enter your marks for chemistry out of hundred: "))

#store the marks in a list
marks = [python, maths, english, physics, chemistry]
total_marks = sum(marks)  # sum() is used to calculate the total marks obtained by the student.
print("\nTotal Marks: ", total_marks)
average_marks = total_marks / len(marks)   # we use len() to get the total number of subjects, and divide the total marks by the number of subjects to get the average marks.
print("\nAverage Marks: ", average_marks)
if marks:
    highest_marks = max(marks)  # max() is used to find the highest marks obtained by the student.
    print("\nHighest Marks: ", highest_marks)
    lowest_marks = min(marks)   # min() is used to find the lowest marks obtained by the student.
    print("\nLowest Marks: ", lowest_marks)
else:
    print("No marks entered.")

#marks in ascending order
print("\nMarks in ascending order")
marks.sort()         #sort() method is used to sort numbers in ascending order.
subjects = ["python", "maths", "english", "physics", "chemistry"]
print(subjects[0], "marks: ", marks[0])
print(subjects[1], "marks: ", marks[1])
print(subjects[2], "marks: ", marks[2])
print(subjects[3], "marks: ", marks[3])
print(subjects[4], "marks: ", marks[4])

#marks in descending order
print("\nMarks in descending order")
marks.reverse()     #reverse() method is used to reverse the order of the list.
print(subjects[0], "Marks: ", marks[0])
print(subjects[1], "Marks: ", marks[1])
print(subjects[2], "Marks: ", marks[2]) 
print(subjects[3], "Marks: ", marks[3])
print(subjects[4], "Marks: ", marks[4])