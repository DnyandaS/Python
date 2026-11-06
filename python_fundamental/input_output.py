# input, output, seprators and end parameters.

name = input("Enter your name: ")
print(name)

# using an int() data type.
age = int(input("Enter oyur age: "))
print(age)

# using a float() data type.
height = float(input("Enter your height: "))
print(height)

# using "+" and "," for ouput.
name_1 = "Hello"
name_2 = "World"
print(name_1,name_2)
print(name_1 + name_2)   # both the outcomes will be same.
print(age,height) # this will give two seprate outputs in the same line, but if you use "+" they will be added.
print(age + height)

## using sep/seprator.
#this is used to edd anything in between the ouputs.
print(name_1, name_2, sep = " ")  # this will add spaces in between.
print(name_1, name_2, sep ="~" )  # this will add negation in between.

## using end parameter.
# it is used to add anything at the end of the output.
print(name_1, name_2, end = "~")   # this will add negation at the end.
