# pure function
#1. pure function is such that when given same input it should produce same output
# 2. should not produce any side effect

# eg  code
def multiply_bt2(li):
    new_list = []
    for item in  li:
        new_list.append(item*2)
    return new_list

print(multiply_bt2([1,2,3]))       #eptable output and no side effect

##
# code which intact with outside world
def multiply_bt2(li):
    new_list = []
    for item in  li:
        new_list.append(item*2)
    return print(new_list)         # same output but this print interacting with outside world

multiply_bt2([1,2,3])            # outside world


