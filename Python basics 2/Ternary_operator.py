# Ternary Operator / Conditional Expression

# Ternary operators also known as conditional expressions are operators that evaluate something based on a condition
# being true or false. It simply allows to test a condition in a single line replacing the multiline if-else making
# the code compact.

# Syntax :

# [on_true] if [expression] else [on_false] 


# Example.....

# suppose you want to check kunal have a permission to send a msg to Dhoni on Facebook but first you need to check
# whether they are friends or not on Facebook.

is_friend = True

is_msg = "Allow to Msg" if is_friend else "Not Allow to Msg"

print(is_msg)
