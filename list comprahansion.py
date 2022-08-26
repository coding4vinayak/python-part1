#list comprahansion



#normal program
my_list = []

for char in "hello":
    my_list.append(char)

print(my_list) # crated list using normal way

# now using list comprahansion

my_list1 = [char for char in "hello" ]

print(my_list1)            #same result using list comp.

#another eh

my_list3 = [num for num in range(0,100)]
print(my_list3)

############ # multioly number by 2

my_list4 = [num*2 for num in range(0,100)]
print(my_list4)

##########
#find even numers in squared number by ^^

my_list5 = [num**2 for  num in range(0,100) if num % 2 ==0]       # num**2 is powr of 2
print(my_list5)                                                   # only even numbers

