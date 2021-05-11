# List is a Data Type in Python 
# in this program we performed List operations 

# Creating List

flipkart = ['mobile', 1, 10.5]

print(flipkart[1])
# List is defined in Square Brackets
# In List you can define any kind of body ex.. int, string, float, and etc....
amazon_cart = ["notebooks", "Laptop"] # In HERE "amazon_cart" is name of list

print(amazon_cart) # In HERE we just simply print the List

print(amazon_cart[0]) # In HERE we just print 1st components of list "notebooks" it's position is 0 

print(amazon_cart[1])# In HERE we just print 2nd components of list "laptop" it's position is 1 


# List Slicing [start : stop : stepover]

amazon_cart = [
    "notebooks",
    "Laptop",
    "grapes",
    "Mobiles",
    "Tickets"
    ]

# List Slicing

amazon_cart[0] = 'grocery' # List is Mutable
new_cart = amazon_cart[:] # [:] it means copy the list OR you can do " amazon_cart.copy() " also
new_cart[0] = 'glue'
print(new_cart) 
print(amazon_cart)

# List Methods 

# adding : .append() is built in function it adds a value at the end of the list.

basket = [1, 2, 3, 4, 5]

basket.append(6) 
print(basket)

# insert : insert(index_no, value) is built in function it insert a value at any index which you give.

basket.insert(1, "kunal")
print(basket) 

# extend : .extend([]) is a built in function it extends a list.

basket.extend([7, 8, 9])
print(basket)

# pop : pop() is a built in function and its remove value from end of the list and pop takes index no that we wanna remove.

basket.pop()
basket.pop(0)
print(basket)

# remove : remove() is a built in function and remove takes value that we wanna remove from our list.

basket.remove(8)
print(basket)

# clear : clear() it removes whatever in the list.

basket.clear()
print(basket)

#  index : index() its just return index no " Syntax : index(value, start, stop) " 

new_list = ['a', 'b', 'c', 'e', 'd', 'f', 'c']
print(new_list.index('b', 0, 2))

# count : count() it's just count numbers of values in list.

print(new_list.count('c'))

# sort : sort() it's just sort a list.

new_list.sort()
print(new_list)

# sorted : sorted() it's a built in function and it also sort a list and it produce new list/array.

print(sorted(new_list))

# reverse : reverse() is reversing the list.
new_list.sort()
new_list.reverse()
print(new_list)

# you can do reverse by slicing. [::-1]
big_basket = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(big_basket[::-1])


# List unpacking

a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
