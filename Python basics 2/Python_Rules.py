# in this file we're gonna see some various python rules / key points.

# 1. Doc String

def test(a):
    '''
    In this function we print 'a' which is 10 and this comment is means DOc String.
    '''
    print(a)


print(test.__doc__)


# Inside the Assignment Expression there is a new operator which is Walrus Operator.

# := that assign a value to a variables as part of a larger expression.

a = 'hellooooooooooo'

if (n := len(a)) > 8:
    print(f"Leanth of a is {n}")
    
while (n := len(a)) > 1:
    print(n)
    a = a[:-1]