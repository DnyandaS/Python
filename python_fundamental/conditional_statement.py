# if-else  statement
num1 = int(input("Enter num1: "))
if num1 >= 0 :
    print("num1 is greater than zero")
else:
    print("num1 is smaller than zero")



# if-elif-else
marks = int(input("Enter marks: "))
if marks >= 90 :
    print("top score")
elif marks >= 70:
    print("average marks")
elif narks >=50:
    print("you should focuse on your studies")
else:
    print("fail")



# nested conditionals
age = int(input("Enter your age: "))
id_card = True
if age >= 18 :
    if id_card :
        print("You may enter")
else:
    print("Recheck your age")