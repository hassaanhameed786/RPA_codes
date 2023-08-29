"""
what assertion are when to use,and how's works
how assertion canbe disable to improve performance
how to debug and test the code


use when use assumption
return val is string
this argument -> is not None

# Role of assertions
Dbugging mke sure your condtions are true otherwise thorw an erroe
Testing
Documents

"""
import pdb
null =None
number = 1
assert number > 0  # return true
x =-11
# assert x >0, f'its less than the 0 or a negative number , ${x}' # give me error
assert null is None
# assert null is not None

assert isinstance(number,int)
number = 42.0

# # class of above number is float
# assert isinstance(number,float)
#
# assert isinstance(number,int), f'is not a class of int,${number}'
#

def get_response(server,ports=(443,80)):
    for port in ports:
        if server.connect(port):
            return server.get()
    return None



print(get_response("realpython.com",()))