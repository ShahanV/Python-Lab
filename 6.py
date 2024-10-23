# Write a program to
# (a) determine frequency of alphabets in a word
# (b) create a list of first-names. Count the number of names that starts with ‘a’

# (a)
word = input("Enter a word: ")
print("Frequency of alphabets: ", {char: word.count(char) for char in set(word)})

# (b)
names = input("Enter a list of names: ").split(",")
count = [names for names in names if names.lower().startswith('a')]
print("Number of names starting with 'a': ", len(count))