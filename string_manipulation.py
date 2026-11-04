# Topic: String Manipulation
# Purpose: Create a program to analyze, modify, and manipulate strings entered by the user.
# Concepts: String indexing, slicing, string methods, searching, replacing, counting characters, and reversing strings.

sentence = input("Enter a sentence: ")

length = len(sentence)    # we use len() to get the length of the string.
print("The length of the sentence is: ", length)

# count vowels and consonants in the sentence
vowels = 0
consonants = 0
for i in sentence:
    if i.lower() in 'aeiou':
        vowels += 1
    elif i.isalpha():
        consonants += 1
    else:
        pass
print("The number of vowels in the sentence is: ", vowels)
print("The number of consonants in the sentence is: ", consonants)

# case conversion
# print the sentence in uppercasei
print("The sentence in uppercase is: ", sentence.upper())
# print the sentence in lowercase
print("The sentence in lowercase is: ", sentence.lower())

# word count
word = sentence.split()  # split() is used to split the sentence into words.
word_count = len(word)
print("The number of words in the sentence is: ", word_count)