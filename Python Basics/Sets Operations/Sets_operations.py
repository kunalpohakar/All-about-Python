# Set
# Set is a unordered collections of a unique objects.

# from typing import List

my_set = {1, 2, 3, 4, 5, 5}

print(my_set)  # it returns only one 5 because it only returns unique set

# print(my_set[0]) # set object does not support indexing.

print(1 in my_set)  # checking 1 is exist in set or not

print(len(my_set))  # measuring the length of a set

print(list(my_set))  # converting set into a list

new_set = my_set.copy()  # simply copying the set
my_set.clear()  # clear set
print(new_set)
print(my_set)  # it returns empty set

# Sets Methods
first_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8, 9, 10}

# .difference() : it shows a difference in between two sets

print(first_set.difference(second_set))  # it shows whats the different in first_set from second_set

# .discard()
first_set.discard(5)  # Remove an element from a set if it is a member.

# If the element is not a member, do nothing.
print(first_set)

# .difference_update()

first_set.difference_update(second_set)  # Remove all elements of second set from first set.
print(first_set)

# intersection() 
print(first_set.intersection(second_set))  # it shows common values between two sets

# .isdisjoint()
print(first_set.isdisjoint(second_set))  # it tell us that two sets are joined or not

# .union()
print(first_set.union(second_set))  # it combined two set and removed duplicates.

# issubset()
one_set = {4, 5}
two_set = {4, 5, 6, 7, 8, 9}

print(one_set.issubset(two_set))  # it tells us that one_set is inside of two_set.

# issuperset()
print(two_set.issuperset(one_set))  # it tells that two_set is superset of one_set.
