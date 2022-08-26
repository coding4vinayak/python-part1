#return is defined function has nothing to return it will say none so we use return
#e.g of none
def sum(num1, num2):
    num1 + num2

    print(sum(3,4))  #we will get nothing

#but using return
def sum(num1, num2):
    return num1 + num2
print(sum(3,4))

print(sum(5,12))

#what return should do
# 1. should do one thing really well
# 2. should return something
#like do something

def sum(num1, num2):
    print('hiiii')
    return num1 + num2

print(sum(9,90))  # this function (sun)  contain hiii also and their opration of adding

#
def sum(num1, num2):
    return num1 + num2
#
#
#
total = sum(4,5)        #no  need print total coz fuction sum in memory above  and  (4 and 5 ) are arguments
print(sum(10,total))           #total defined above
#another way
print(sum(10,sum(4,5)))         #neat and clean

#
# multi define
def sum(num1, num2):
 def another_func(num1,num2):
    return num1 + num2
 return another_func(num1,num2)


total = sum(10,20)
print(total)

#more clean
def sum(num1, num2):
 def another_func(n1,n2):           #these n1 and n2 does care
    return n1 + n2                  # of final print
 return another_func(num1,num2)


total = sum(10,20)

#no code run after 1st return
def sum(num1, num2):
 def another_func(n1,n2):           #these n1 and n2 does care
    return n1 + n2                  # of final print
 return another_func(num1,num2)    #only this return will run
 return 5               #  these return nrver run
 return ("hello")       #   no run


total = sum(10,20)


#exerssie tesla



