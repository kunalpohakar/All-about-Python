# Tuple
# () it denotes that Tuple
# Tuple is immutable.

my_tuple = (1, 2, 3, 4, 5, 4)
print(my_tuple)

print(my_tuple[1]) # you can access tuple element by their index values.

# Tuple is just like a list 
# Tuple Slicing

print(my_tuple[0:5:2]) # [start : stop : stepover]

x,y, *other = (6, 7, 8, 9, 10)

print(x)
print(other)

# Tuple have only Methods
# count() and index()

print(my_tuple.count(4)) # count() : it counts how many values in there tuple

print(my_tuple.index(5)) # index() : it shows the index of values

print(len(my_tuple)) # len() : shows length of a tuple.
