#iterable  is collection of items it can be set , tuple , dictionary ,list , sting
# why iterable coz they can be iterated
# iterated means = one by one cheack each item in collection

user = {
   ' name' : 'golam',
    'age' : 5006 ,
    'can_swim ': False
}

for item in user:
    print(item)

#but we want values also there are 3 ways

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

#but if we want  unpack means not in tuple () than
user2 = {
   ' name' : 'golam',
    'age' : 5006 ,
    'can_swim ': False
}

for item in user2.items():
    key, value = item;
    print(key , value)

#another methos

for key, value in user2.items():
    print(key, value)