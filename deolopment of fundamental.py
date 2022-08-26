#clean
#readablity
#predactiblity
#DRY  =  do  not repet yourself



#exersise find duplicate


#cheack for duplicates in list

some_list = [ 'a', 'b', 'c', 'b', 'e','e']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)