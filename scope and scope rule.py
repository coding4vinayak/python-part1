#scope
# scope = what veriables do i have access to?
# print(name())  #name error scope not defined
if True:                 #this block has differant scope
    x =10

def some_func():           #this block has differant scope
    total = 100
    print(x)


#scope rule

a = 1                # but this is on other global scope not under any block

def confusion():
    a = 5             # this a is in dofferant univers of function confusion
    return a

print(a)
print(confusion())

#rules of scope
# 1 . start with local scope  eg . a in def is local scope
# 2. is there any parant scope eg a in def parant a is parant sope
#eg
a = 1                # but this is on other global scope not under any block

def parant():            #parant scope
  a = 10
  def confusion():
    return a
  return confusion()


print(parant())
print(a)

# 3 .  is there any global scope
#eg

a = 1                # but this is on other global scope not under any block

def parant():            #parant scope

  def confusion():
    return a
  return confusion()


print(parant())       # both value use global scope
print(a)


# 4. built in python functions
#eg

a = 1                # but this is on other global scope not under any block

def parant():            #parant scope

  def confusion():
    return sum        ### built in function
  return confusion()


print(parant())       # both value use global scope
print(a)

