# Write a program to
# (a) print out all colors from color-list1 not contained in color-list2
# (b) Write a program to remove duplicates from a list
# (c) Write a program to check whether a list is empty or not

# (a)
color1 = set(input("Enter the color set 1: ").split(","))
color2 = set(input("Enter the color set 2: ").split(","))
print(list(color1 - color2))

# (b)
deduplicated_list = list(set(item.strip() for item in color1))
print("List after removing duplicates: ", deduplicated_list)

# (c)
print("Is color set 1 empty: ", not color1)