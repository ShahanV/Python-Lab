# List Comprehension:
# (a) Generate positive list of numbers from a given list of numbers
# (b) Generate a list with square of numbers from a given list
# (c) Form a list containing vowels from a given word
# (d) Generate a list of numbers by removing even numbers from a given list
# (e) Display leap years from current year to a future year entered by user

# (a)
list = [-6, -2, 5, 6, 8]
print("Positive numbers: ", [i for i in list if i > 0])

# (b)
print("Squares: ", [i * i for i in list])

# (c)
word = input("Enter a word: ")
print("List containing vowels: ", [i for i in word if i.lower() == 'a' or i.lower() == 'e' or i.lower() =='i'
or i.lower() == 'o' or i.lower() == 'u'])

# (d)
print("Odd numbers: ", [i for i in list if i % 2 != 0])

# (e)
future = int(input("Enter the future year: "))
print("Leap years: ", [i for i in range(2024, future) if i % 4 == 0 and (i % 400 == 0 or i % 100 != 0)])