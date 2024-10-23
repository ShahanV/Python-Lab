# Write a program to
# (a) Write a program to check if a given key already exists in a dictionary
# (b) Write python program to merge two dictionaries
# (c) Write a program to sort a dictionary in ascending and descending order
# (d) Write a program to create an inverted dictionary

first_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
second_dict = {'date': 4, 'blueberry': 5}

# (a)
key_to_check = 'banana'
print("Key exists: ", key_to_check in first_dict)

# (b)
merged = first_dict.copy()
merged.update(second_dict)
print("Merged dictionary:", merged)

# (c)
sorted_asc = dict(sorted(first_dict.items()))
sorted_desc = dict(sorted(first_dict.items(), reverse=True))
print("Ascending order:", sorted_asc, "| Descending order:", sorted_desc)

# (d)
print("Inverted dictionary:", {v: k for k, v in first_dict.items()})