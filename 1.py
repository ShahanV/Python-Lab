# Write a program to get a string from the user
# (a) replace all occurrences of first character with ‘$’, except first character
# (b) Create a string from given string where first and last characters exchanged

# (a)
string = input("Enter a string: ")
first_character = string[0]
print("String after replacing occurrences of first character: ", first_character + string[1:].replace(first_character, "$"))

# (b)
print("String after exchanging first and last characters: ", string[-1] + string[1:-1] + string[0])