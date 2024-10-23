# Enter 2 collections of integers. Check
# (a) Whether they are of the same length
# (b) whether they sums to the same value
# (c) whether any value occur in both

# (a)
list1 = input("Enter first list of integers: ").split(",")
list2 = input("Enter second list of integers: ").split(",")
print("Does the collection have same length: ", len(list1) == len(list2))

# (b)
print("Does the collection sum to the same value: ", sum(map(int, list1)) == sum(map(int, list2)))

# (c)
print("Common elements: ", list(set(list1) & set(list2)))
print("Does any value occur in both: ", bool(list(set(list1) & set(list2))))