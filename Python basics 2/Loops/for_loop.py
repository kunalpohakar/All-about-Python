# For Loop
# iterables - list, dictionary, set, tuple, or string this are iterables.
# iterates : one by one check each item in the collections.
# syntax :
# for variable in object:
#       body of loop

user = {
    'name': 'kunal',
    'age': 18,
    'role': 'senior developer'
}

for item in user:
    print(item)  # here it print only keys.


for item in user.items():
    print(item)  # here we print whole dictionary but it gives output in tuple format.


for key, value in user.items():
    print(key, value)
    # here we print whole dictionary without tuple format.

for item in user.values():
    print(item)
    # here we print only values


# WAP that gives sum of the elements of list.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
for item in my_list:
    counter += item
print(counter)


# innumerate
'''
A lot of times when dealing with iterators, we also get a need to keep a count of iterations. Python eases the 
programmers’ task by providing a built-in function enumerate() for this task. Enumerate() method adds a counter to an 
iterable and returns it in a form of enumerate object. This enumerate object can then be used directly in for loops 
or be converted into a list of tuples using list() method. 

Syntax: 

enumerate(iterable, start=0)

'''
# here we find the index no of 50
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is: {i}")