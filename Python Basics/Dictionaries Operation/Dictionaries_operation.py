# Dictionary is a unordered key|value pair.
# {} denotes it's a Dictionary
# syntax is : Dictionary_name : {kay : value, kay : value}
# Dictionary is a mutable
# A dictionary keys always has to be an immutable.

user = {
    'a' : [1, 2, 3],
    'b' : 'Hi',
    'c' : True
    }
  
# print(dictionary)

# if you wanna check that a particular key is exist in a dictionary or not without getting an error.
# use get() it's check thar the key is exist in a dictionary or not.

print(user.get('x'))


# its means : Hey grab the 'x' from the user dictionary if 'x' doen't exist in the user dictionay then use 55.
print(user.get('x', 55)) # In case it does'n exist add a default value.



user2 = dict(name = 'jojo') # This is a another way to creating a dictionary.
print(user2)


print('x' in user) # it means : 'x' does exist in user.

# if you wanna check keys does exist or not
print('x' in user.keys())

# if you wanna check values 
print('Hi' in user.values())

# if you wanna check items 
print(user.items())

# if you wanna copy the dict

copy_user = user.copy()
print(user.clear())
print(copy_user)

# if you wanna a clear your dict
print(user.clear())


user = {
    'a' : [1, 2, 3],
    'b' : 'Hi',
    'c' : True
    }


# if you wanna remove key 
print(user.pop('c')) # it returns value of that key.
print(user)

# popitem() : it removes item from a dict randomly.
print(user.popitem())
print(user)

# if you wanna update a key item or udate a value

user.update({'a' : [4, 5, 6]})
print(user)
user.update({'b' : [7, 8, 9, 10]})
print(user)

