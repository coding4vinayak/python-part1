#logical oprator and exercise

# types  of logical oprtor
'''  or , and , > , < , == , NOT ,
'''


print(4>5)
print(5<6)
print(5==4)

print('a' > 'b')    #ascii code
print('a' > 'A')


print(1<2<3<4)
print(1<2>3<4)

print(1>= 0)
print(1 <= 0)
print(0 <= 0)


print( 0 != 0)

print(not(True))
print(not(1==1))


#eg

is_magician = True
is_expert = False

if is_magician and  is_expert:
    print(' you are a master magician')
elif is_magician and not is_expert:
    print("at lest you're getting there")
elif not is_magician:
    print('you need magic power')
