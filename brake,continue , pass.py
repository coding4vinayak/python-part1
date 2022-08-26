# break works for while as well as for loop
my_list = [1,2,3]
for item in my_list:
    print(item)
    break


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break

#agi  start looping using continue
my_list = [1,2,3]
for item in my_list:
    print(item)
    continue


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue

my_list = [1,2,3]
for item in my_list:
    print(item)
    pass         #pass to next line

#pass use when nothing is coded and move on to next block eg


#eg
my_list = [1,2,3]
for item in my_list:
 # still thinking about what to code but cant live empty will give error so use pass will go to next block
    pass


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    break


