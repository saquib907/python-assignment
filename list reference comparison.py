list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# Compare values vs. compare memory locations
print("Same values?:", list1 == list2)        # True
print("Same object?:", list1 is list2)        # False (separate lists)
print("Same object?:", list1 is list3)        # True (same list)