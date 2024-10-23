# Write a program to count the occurrences of
# (a) each word in a line of text
# (b) character frequency in a sentence

from collections import Counter

# (a)
text = input("Enter a line of text: ")
word = text.split()
set = set(word)
print("Word occurrences: ", {word:word.count(word) for word in set})

# (b)
sentence = input("Enter a sentence: ")
char_count = Counter(char.lower() for char in sentence if char.isalpha())
print("Character frequency:", dict(char_count))