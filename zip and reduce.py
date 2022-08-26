# zip
#zips two ierable
#eg

my_list = [1,2,3]
your_list = (10,20,30)   # even its tuple it zips
their_list = [5,4,9]      # i can n number of list and tuple to zip

print(list(zip(my_list,your_list)))     # its zip two iterable in 2 sets
print(list(zip(my_list,your_list,their_list)))         # any number of list zips#


#####################################

# reduce
# reduce all values in requird on vale or something like that

my_list2 = [1,2,3]
from functools import  reduce

def accumlator (acc , item):
    print(acc , item)
    return acc + item

print(reduce(accumlator,my_list2, 0))         # 0 is starting value of acc
# lets change staring acc value tp 10
print(reduce(accumlator,my_list2, 10))    # acc starts from 10

print(my_list2)  # also is pure function
