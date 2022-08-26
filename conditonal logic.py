#conditional logic
is_old = True
is_licenced = True

if is_old:
    print("you are old enough "
          "to drive!")

print('checheck')   #seprate code for eg


is_old2 = False
is_licenced2 = True

if is_old2:
    print("you are old enough "
          "to drive!")              #nothing prints above code

else:
    print('you are not '
          'allowed to drive')


is_old3 = True
is_licenced3 = True

if is_old3:
    print("you are old enough "
          "to drive!")              #nothing prints above code

else:
    print('you are not '
          'allowed to drive')
print('hello')


is_old4 = False
is_licenced4 = True             #if false else will print

if is_old4:
    print("you are old enough "
          "to drive!")
elif is_licenced4:
    print('you can drive now')
else:
    print('you are not '
          'allowed to drive')



is_old5 = False
is_licenced5 = False

if is_old5 and is_licenced5:                    #both needed to true
    print('you are old enough to drive')

else:
    print('you cant drive')

#indentaion or spacing