##    Generator
##
##    Functions with yield expression will be compiled into a
##    generator object which supported the iterator interface.
##  
##


def gen_fn(n):
    for i in range(n):
        #return the value and then suspend
        yield i ** 2

#test
for i in gen_fn(5):
    print(i)

#output     0
#           1
#           4
#           9
#           16
