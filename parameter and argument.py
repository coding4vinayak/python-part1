#parameters
#parameters are used when we define the function
def say_hello(name , emoji):           #name and emoji are parameter
    print(f'helllooo {name}{emoji}')


#argument    also call positional argumet coz position matters
#argument are used when we call the function
say_hello('vinayak',' 😂')

#also calls  =  call and invoke function

say_hello('dan','🤣')
say_hello('emily', '❤')


#default parameter and keyword argument
# we inove parameter at default location  thats why called positioning argument


#keyword argument

say_hello(emoji='💋', name = 'raj')    #not need to worry about positioning

#default parameter if forgot to mention fuction than default will be used
#eg
def say_hello(name= 'darth vedar', emoji='🐱‍'):
    print(f'helloo {name}  {emoji}')

say_hello(emoji='💋', name = 'raj')    # if function defined than they will print
say_hello()                  # otherwise defalit will print eg darth vedar
say_hello('vinayak')         #name defined but emoji no so print default