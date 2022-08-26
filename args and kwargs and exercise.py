#args and #kwargs
#arguments and keword arguments
# special charachters
#   *args        **kwargs
#eg

def super_func(*args):        #this * can accept any number for positional argument without * it accept only one
    print(*args)               #we can print without * to get tuple ()
    return sum(args)
print(super_func(1,2,3,4,5))

#kwargs

def super_func(*args, **kwargs):        #this * can accept any number for positional argument without * it accept only one
    print(kwargs)
    return sum(args)
print(super_func(1,2,3,4,5 , num1 = 5 , num2 = 10))

#
def super_func(*args, **kwargs):        #this * can accept any number for positional argument without * it accept only one
    total = 0
    for items in kwargs.values():      # we are looping here coz *kwargd give us dictionary
     total += items
    return sum(args) + total
print(super_func(1,2,3,4,5 , num1=5 ,num2 =10))


####3
#rules = params , *args , default parameters , **kwargs    in this order
#eg def su_func( name , *args, i='hi' , **kwargs) in this order


# exercise find highest even in list
def highest_evens(li):
    evens = []
    for items in li:
        if items % 2 == 0:
            evens.append(items)
    return max(evens)
print(highest_evens([2,10,2,3,4,8,11]))

#
#
#
/