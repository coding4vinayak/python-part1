#functions
#we can creat our own functions by defining them
#def = define function
def say_hello():
    print('helloooo')
say_hello()


#eg
#gui

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#1 iterate over picture
# if 0 -> print " "
# if 1 -> print *

def our_tree():             #created our own function and has following code in it
 for row in picture:
   for pixel in row:
     if (pixel == 1):
       print("*", end= "")
     else:
       print(" ", end= "")
   print("")


our_tree()           #now only run our function automatically run code in it
our_tree()
our_tree()

#location on memory
print(our_tree)