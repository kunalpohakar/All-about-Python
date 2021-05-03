# Dictionary is a unordered key|value pair.
# {} denotes it's a Dictionary
# syntax is : Dictionary_name : {kay : value, kay : value}
# A dictionary keys always has to be an immutable.

dictionary = {
    'a' : [1, 2, 3],
    'b' : 'Hi',
    'c' : True
    }
  
# print(dictionary)

# if you wanna check that a particular key is exist in a dictionary or not without getting an error.
# use get() it's check thar the key is exist in a dictionary or not.

print(dictionary.get('a')) 