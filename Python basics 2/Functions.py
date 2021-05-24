import math
# Functions
# syntax of creating a function
'''
def function_name():
    body of function
    
function_name()

'''

def say_hello():
    print('Hellooooo')
    
say_hello()

'''
Functions allow us to keep a code DRY and you can re-use and call a function multiple times. 
'''

# Arguments vs Parameters

# Parameters we give when creating a function and 
# Arguments we give when we call the function

# parameters
def main(name, emoji):
    print(f'Hello {name} {emoji}')

# Arguments
main('Kunal', ':)')


# Exercise Time

def highest_even(li):
    evens = []
    for i in li:
        if i%2 == 0:
            evens.append(i)
    print(max(evens))
    print(min(evens))

highest_even([10,2,3,4,8,11])