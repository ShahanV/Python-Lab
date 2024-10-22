# Write a program to
# (a) creates a single string separated with space from two strings by swapping the character at position 1
# (b) Create a list of colours from comma separated list of colour names entered by user. Print alternate colors

# (a)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
new_string = string1[0] + string2[1] + string1[2:] + " " + string2[0] + string1[1] + string2[2:]
print("String after swapping characters at position 1: ", new_string)

# (b)
colors = input("Enter a list of colors seperated by comma: ")
colors_list = colors.split(",")
print("Alternate colors are: ")
for i in range(0, len(colors_list), 2):
    print(colors_list[i])