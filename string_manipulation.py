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
    if i.lower() in 'aeiou' or i in 'AEIOU':
        vowels += 1
    elif i.isalpha():
        consonants += 1
    else:
        pass
print("The number of vowels in the sentence is: ", vowels)
print("The number of consonants in the sentence is: ", consonants)

# case conversion
# print the sentence in uppercase
print("The sentence in uppercase is: ", sentence.upper())
# print the sentence in lowercase
print("The sentence in lowercase is: ", sentence.lower())

# word count
word = sentence.split()  # split() is used to split the sentence into words.
word_count = len(word)
print("The number of words in the sentence is: ", word_count)

# see how many times a specific character appears in the sentece.
search_char = input("Enter a character to search for: ")
char_count = sentence.count(search_char)
print("The character '", search_char, "' appears ", char_count, " times in the sentence.")

# replace string
replace_str = input("Enter a string to replace: ")
new_str = input("Enter the new string: ")
modified_sentence = sentence.replace(replace_str, new_str)
print("The modified sentence is: ", modified_sentence)

# reverse the sentence
reversed_sentence = sentence[::-1]  # slicing to reverse the string
print("The reversed sentence is: ", reversed_sentence)