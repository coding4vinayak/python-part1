#types of functions
# map , filter ,zip ,reduce

#######
 #map
 #eg

def multiply_by2(item):
    return item*2

print(map(multiply_by2, [1,2,3]))        # this will give location in mamory
print(list(map(multiply_by2,[1,2,3])))   # will give answer

# eg what map does

my_list = [1,2,3]
def multiply_by2(item):
    return item*2

print(map(multiply_by2, my_list))        # this will give location in mamory
print(list(map(multiply_by2,my_list)))   # pure function , immutable
print(my_list)     # you can see map doesnt modify original list its creat own list
                   # this is pure function does not affect outside


######################################

#filter
# filer ou data for us

my_list1 = [1,2,3]
def only_odd(item):
    return item % 2 != 0

print(filter(only_odd,my_list1))  # show location of object
print(list(filter(only_odd,my_list1)))   # its filter out even number and shows only odd.

print(my_list1)     # pure function does affect outside

## very very cool