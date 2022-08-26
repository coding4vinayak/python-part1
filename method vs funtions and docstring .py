#methods vs functions

#fuctions we have
# list , print , max ,min , input and def some_random

#methods we use .after
#like  capitalize , casefold, count,find , format , index

# method has to own by something  so  whaterver left to dot owns method
 # "helllo".capitalize()



#
#
#docstring
#docstring allow to comment in function such way that it shows info while using function
#eg

def test(a):
    '''

   info : this function test and print param a          

    '''                       #this is docstring will be shown info about param
    print(a)

test('!!!!!')
#test()

help(test)

print(test.__doc__)

