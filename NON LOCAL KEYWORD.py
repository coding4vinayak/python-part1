#non local keyword
def outer():
    x = 'local'               # this parant scope is replaced by nonlocal
    def inner():
        nonlocal x             #this is non local
        x = 'nonlocal'
        print("inner:",x)

    inner()
    print("outer:",x)

outer()                      # this will also print nonlpcal coz it is been modified

###
####

# why we need scop