##    Generator
##
##    Functions with yield expression will be compiled into a
##    generator object which supported the iterator interface.
##  
##

##  demo1
##  generator function
def generator(n):
    for i in range(n):
        #return the value and then suspend
        yield i ** 2

#test
for i in generator(5):
    print(i)

#output     0
#           1
#           4
#           9
#           16




##  demo2
##  generator expression
genexp = (i**2 for i in range(5))

#test
for i in genexp:
    print(i)
    
#output     0
#           1
#           4
#           9
#           16
