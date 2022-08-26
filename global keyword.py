# GLOBAL KEYWORD

#EG of local

A = 10
def confusion(b):            # confusion  parameter b is consider local parameter in def function
    print(b)
    a = 90

confusion(300)

#global  keyword

total = 0

def count():
    global total                #global keyword be used here by mentionaning global
    total += 1
    return  total

count()
count()
print(count())         #counted 3 times

# above confusing make it simpler

total = 0

def count(total):
    total += 1
    return total

print(count(count(count(total))))    #here we go same result


