# truthy ans falsy

is_old4 = 'hello'       #these values get converted in truse and false by bool()
is_licenced4 = 5

print(bool('helllo'))
print(bool(5))


if is_old4:
    print("you are old enough "
          "to drive!")
elif is_licenced4:
    print('you can drive now')
else:
    print('you are not '
          'allowed to drive')

#eg 2
is_old5 = 'hello'       #these values get converted in truse and false by bool()
is_licenced5 = 5

print(bool(''))
print(bool(0))               #falsy


if is_old5:
    print("you are old enough "
          "to drive!")
elif is_licenced5:
    print('you can drive now')
else:
    print('you are not '
          'allowed to drive')




'''All values are considered "truthy" except for the following, which are "falsy":

None
False
0
0.0
0j
decimal.Decimal(0)
fraction.Fraction(0, 1)
[] - an empty list
{} - an empty dict
() - an empty tuple
'' - an empty str
b'' - an empty bytes
set() - an empty set
an empty range, like range(0)
objects for which
obj.__bool__() returns False
obj.__len__() returns 0
A truthy" value will satisfy the check performed by if or while statements. We use "truthy" and "falsy" to differentiate from the bool values True and False.
'''