# == cheacks equaliyu

print(True == 1) # true
#explantion
print(True == bool(1)) #its become true


print('' == 1  )  #false
print('1' == 1 )  #false string vs int


print([] == 1)   #false
print(10 == 10.0 )  #true
print([] == [])   #true


#is  chacks  if location in memory where this vlaue is stored is same


print(True is 1)

print('' is 1  )
print('1' is 1 )

print([] is 1)
print(10 is 10.0 )
print([] is [])

# what is do


print(True is True)

print('' is '' )
print('1' is '1')

print([] is [])  #false bcaz every thim list is created its addes in differant meomary thats why they are not
# at same location
print(10 is 10 )
print([1,2,3] is [1,2,3]) #false coz diffeernat list
