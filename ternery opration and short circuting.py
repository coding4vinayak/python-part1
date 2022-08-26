#ternery oprator   or conditional opration


#   condition_if _true if condition else condition_if_else

# eg

is_friend = True
is_friend = False       #redeclaired
can_message = 'message allowed' if is_friend else ' not allowed allowed to message'
print(can_message)


#short circuiting
# use of OR
# if either one is true than steatment is true

#eg

my_friend = True
my_user  = True

if my_friend or my_user:
    print("best friend forever")

if False or my_user:
    print('best friend forever')
