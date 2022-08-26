#contunue

my_list = [1,2,3]            #lop by for
for item in my_list:
    print(item)

i  = 0
while i < len(my_list):             #loop by while
    print(my_list[i])
    i += 1


while True:
    input('say something:')
    break                        #if you not add brak try


while True:
    response = input('say something:')
    if (response == "bye" ):
        break