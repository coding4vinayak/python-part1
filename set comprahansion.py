#  just differance is list [] to set {}

my_set = {char for char in "hello" }
print(my_set)


#######
my_set2 = {num for num in range(0,100)}
print(my_set2)

##############
#dictionary comp

simple_dict = {
    'a' : 1,
    'b' : 2
}
my_dict = {key:value**2 for key,value  in simple_dict.items()}
print(my_dict)

my_dict = {key:value**2 for key,value  in simple_dict.items() if value%2 ==0}

my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)
