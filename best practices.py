'''

some dictionaries best practices and practices

'''
import pdb              # good for debugging
print(dir({}))
print(dir([]))

example ={'color': 'red', 'fruit': 'apple', 'species': 'dog'}
for k in example:
    print(k, example[k])


for value in example.values():
    print(value)

print(example.keys())

for item in example.items():
    print(type(item))

prices = {'apple': 12, 'orange': 15, 'banana':10}
a_dict = {'apple': 12, 'orange': 15, 'banana':10}

# how to swap val->key and vice versa
new ={}
for key,val in a_dict.items():
        new[val] = key
        print(new)

for key in prices:
    prices[key] = prices[key] + 12

# dictionary comprehension is a good feature to do

invoices = ["Pk2302089","Pk2302088", "Pk2302087","Pk2302086"]
dates = ["20/05/2023","12/09/2022","20/08/2023","29/05/2023"]

# how can zip two lists in a dictionary
invoice_by_date = {key:value for key, value in zip(dates,invoices)}

# if i want to change the value -> to key and vice versa
invoice_by_date= {value:key for key,value in zip(invoices,dates)}
incomes = {'ali':11000, 'ahmed': 12313, 'bilal': 99999}

pdb.set_trace()

# sorted the incomes by the by value
incomes = {'ali':1100000, 'ahmed': 12313, 'bilal': 99999}
srted_incomes = {k: incomes[k] for k in sorted(incomes)}
def by_value(item):
    return item[1]

pdb.set_trace()

# dictionary packing way
print('unpcking dictionaries')
{**invoice_by_date,**incomes}

print('before sorted ', incomes)
for k,v in sorted(incomes.items(),key=by_value):
    print(k,v)

# how the backend work on popitem  in dictionary
dict_rand = {'a':1, 'b':2, 'c':3}
while True:
    try:
        item = dict_rand.popitem()
        print(item)
    except KeyError:
        print('the dictionary is now empty')
        break

''' 
use for multiple run same code 
'''
from itertools import cycle
num= 12
for k, in cycle(incomes.values()):
    if num ==0:
        break
    num =-1
    print(k)


pdb.set_trace()
# Chained the invoices and dates dictionary into one dictionary
from collections import ChainMap
Invoice_dt =ChainMap(dates,invoices)

Invoice_dt
